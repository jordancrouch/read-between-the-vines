from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from django.views.generic.edit import FormMixin, UpdateView

from .forms import CommentForm
from .models import Books, Comment
from .utils import get_published_books


# Create your views here.
class BooksList(generic.ListView):
    queryset = get_published_books()
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["currently_reading_books"] = get_published_books(category="CR")
        context["to_be_read_books"] = get_published_books(category="TBR")
        context["finished_reading_books"] = get_published_books(category="FR")

        return context


class BooksArciveList(generic.ListView):
    # queryset = Books.objects.filter(status=1).order_by("-created_on")
    queryset = get_published_books(category="FR", limit=None)
    template_name = "books/archive.html"
    context_object_name = "books_archive"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BookDetail(FormMixin, generic.DetailView):
    model = Books
    template_name = "books/book_detail.html"
    context_object_name = "book"
    form_class = CommentForm

    def get_queryset(self):
        return Books.objects.filter(status=1)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs.get("slug"))

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.book = self.object
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()

        comments = book.comments.all().order_by("-created_on")
        comment_count = book.comments.filter(approved=True).count()
        comment_form = CommentForm

        context["comments"] = comments
        context["comment_count"] = comment_count
        context["comment_form"] = comment_form

        return context


class CommentEditView(UpdateView):
    model = Comment
    form_class = CommentForm
    pk_url_kwarg = "comment_id"
    http_method_names = ["post"]

    def dispatch(self, request, *args, **kwargs):
        self.book = get_object_or_404(Books, slug=self.kwargs["slug"], status=1)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.post
        comment.approved = False
        comment.save()
        messages.success(self.request, "Comment updated!")
        return HttpResponseRedirect(reverse("books:book_detail", args=[self.book.slug]))

    def form_invalid(self, form):
        messages.error(self.request, "Error updating comment!")
        return HttpResponseRedirect(reverse("books:book_detail", args=[self.book.slug]))

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
