from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import FormView
from django.views.generic.edit import FormMixin, UpdateView

from .forms import CommentForm, ContactForm, ReadingProgressForm
from .models import Books, Comment, ReadingProgress
from .utils import get_published_books


class BooksList(generic.ListView):
    """
    View for displaying a list of books grouped by reading category.

    Published books are grouped into three categories:
    - Currently Reading (CR): average reading progress is also calculated
    - To Be Read (TBR)
    - Finished Reading (FR)

    Attributes:
        queryset (QuerySet): initial published books.
        template_name (str): the template used to render the book list(s).
    """

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
    """
    View for displaying all books that are 'finished reading'.

    Attributes:
        queryset (QuerySet): all published books in the Finished Reading category.
        template_name (str): the template used to render the book archive list.
        context_object_name (str): the variable name used in the template context.
        paginate_by (int): the number of books to display per-page.
    """

    queryset = get_published_books(category="FR", limit=None)
    template_name = "books/archive.html"
    context_object_name = "books_archive"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BookDetail(FormMixin, generic.DetailView):
    """
    Displays the detail page for an individual book.

    This view handles GET and POST requests.
    GET shows the book details, existing comments, and the user's reading progress.
    POST handles the following two forms:
    - CommentForm: for submitting a new comment.
    - ReadingProgressForm: for submitting/updating reading progress.

    Attributes:
        model (Model): the Books model used for retrieving the book instance.
        template_name (str): the template used to render the book detail page.
        context_object_name (str): the variable name used in the template context.
        form_class (ModelForm): the form class used for submitting comments.
    """

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
        context["progress"] = user_progress

        return context


class CommentEditView(UpdateView):
    """
    Displays an individual comment for editing.

    Requests are restricted to POST only and re-approves the comment on submission.
    Only the comment author can update their comment.

    Attributes:
        model (Model): the Comment model used for retrieving/updating the comment.
        form_class (ModelForm): the form class used for submitting comments.
        pk_url_kwarg (str): the URL keyword argument used to look up the comment's primary key.
        http_method_names (list): restrict requests to POST only.
    """

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
    """
    Deletion of an individual comment by the comment's author.

    POST requests only. Comment author's are allowed to delete their own comment(s).
    After a comment is deleted, the user is redirected back to the book's detail page.

    Attributes:
        post (method): handles the deletion of a comment based on the user.
    """

    def post(self, request, slug, comment_id):
        book = get_object_or_404(Books, slug=slug, status=1)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user:
            comment.delete()
            messages.success(request, "Comment deleted!")
        else:
            messages.error(request, "You can only delete your own comments!")

        return HttpResponseRedirect(reverse("books:book_detail", args=[book.slug]))


class ReadingProgressDeleteView(View):
    """
    Deletion of a user's reading progress.

    POST requests only. Reading progress author can delete their own progress.
    After progress has been deleted, the user the redirected back to the book's detail page.

    Attributes:
        post (method): handles the deletion of reading progress based on the user.

    """

    def post(self, request, slug, progress_id):
        book = get_object_or_404(Books, slug=slug)
        reading_progress = get_object_or_404(ReadingProgress, pk=progress_id, book=book)

        if reading_progress.user == request.user:
            reading_progress.delete()
            messages.success(request, "Reading progress deleted successfully!")
        else:
            messages.error(request, "You can only delete your own progress.")

        return HttpResponseRedirect(reverse("books:book_detail", args=[book.slug]))


class ContactView(FormView):
    """
    Displays the contact page and contact form.

    Attributes:
        template_name (str): the template used to render the contact page.
        form_class (ModelForm): the form class used for the contact form.
        success_url (str): the URL to redirect users to after a successful form submission.

    """

    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        messages.success(self.request, "Your message has been sent!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your submission.")
        return super().form_valid(form)
