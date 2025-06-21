# from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Books
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


class BookDetail(generic.DetailView):
    model = Books
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get_queryset(self):
        return Books.objects.filter(status=1)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()

        return context
