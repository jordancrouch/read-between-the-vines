# from django.shortcuts import render
from django.views import generic

# from .models import Books
from .utils import get_published_books


# Create your views here.
class BooksList(generic.ListView):
    # queryset = Books.objects.filter(status=1).order_by("-created_on")
    queryset = get_published_books()
    template_name = "books/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["currently_reading_books"] = get_published_books(category="CR")
        context["to_be_read_books"] = get_published_books(category="TBR")
        context["finished_reading_books"] = get_published_books(category="FR")

        return context
