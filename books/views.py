from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.views import View, generic
from django.views.generic.edit import FormMixin, UpdateView

from .forms import CommentForm, ReadingProgressForm
from .models import Books, Comment, ReadingProgress
from .utils import get_published_books


# Create your views here.
class BooksList(generic.ListView):
    queryset = get_published_books()
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        currently_reading_books = get_published_books(category="CR")
        for book in currently_reading_books:
            avg = book.progress.aggregate(avg=Avg("percentage"))["avg"] or 0
            book.avg_progress = round(avg)

        to_be_read_books = get_published_books(category="TBR")
        finished_reading_books = get_published_books(category="FR")

        context["currently_reading_books"] = currently_reading_books
        context["to_be_read_books"] = to_be_read_books
        context["finished_reading_books"] = finished_reading_books

        return context


class BooksArchiveList(generic.ListView):
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

        if "comment_submit" in request.POST:

            comment_form = self.get_form()

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.book = self.object
                comment.save()
                messages.success(request, "Comment submitted and awaiting approval.")
                return self.form_valid(comment_form)
            else:
                messages.error(request, "There was an error submitting your comment.")
                return self.form_invalid(comment_form)

        elif "progress_submit" in request.POST:
            if not request.user.is_authenticated:
                messages.error(request, "You must be logged in to track progress.")
                return self.get(request, *args, **kwargs)

            instance = ReadingProgress.objects.filter(
                user=request.user, book=self.object
            ).first()
            progress_form = ReadingProgressForm(request.POST, instance=instance)
            if progress_form.is_valid():
                progress = progress_form.save(commit=False)
                progress.user = request.user
                progress.book = self.object
                progress.save()

                avg_progress = (
                    self.object.progress.aggregate(avg=Avg("percentage"))["avg"] or 0
                )
                if (
                    avg_progress >= 80
                    and self.object.category == Books.ReadingStatus.CURRENTLY_READING
                ):
                    self.object.category = Books.ReadingStatus.FINISHED_READING
                    self.object.save()

                messages.success(request, "Reading progress updated!")
            else:
                messages.error(request, "There was an error updating your progress.")
            return self.get(request, *args, **kwargs)

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()

        context["comments"] = book.comments.all().order_by("-created_on")
        context["comment_count"] = book.comments.filter(approved=True).count()
        context["comment_form"] = self.get_form()

        user_progress = None
        if self.request.user.is_authenticated:
            user_progress = ReadingProgress.objects.filter(
                user=self.request.user, book=book
            ).first()
            progress_form = ReadingProgressForm(instance=user_progress)
        else:
            progress_form = None

        raw_average = book.progress.aggregate(avg=Avg("percentage"))["avg"] or 0
        average_progress = round(raw_average, 2)

        context["progress_form"] = progress_form
        context["user_progress"] = user_progress
        context["average_progress"] = round(average_progress)

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
        comment.book = self.book
        comment.approved = False
        comment.save()
        messages.success(self.request, "Comment updated!")
        return HttpResponseRedirect(reverse("books:book_detail", args=[self.book.slug]))

    def form_invalid(self, form):
        messages.error(self.request, "Error updating comment!")
        return HttpResponseRedirect(reverse("books:book_detail", args=[self.book.slug]))

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)


class CommentDeleteView(View):
    def post(self, request, slug, comment_id):
        book = get_object_or_404(Books, slug=slug, status=1)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user:
            comment.delete()
            messages.success(request, "Comment deleted!")
        else:
            messages.error(request, "You can only delete your own comments!")

        return HttpResponseRedirect(reverse("books:book_detail", args=[book.slug]))
