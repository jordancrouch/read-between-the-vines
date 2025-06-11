from django.shortcuts import render
from django.views import generic

from .models import Books
from .utils import get_published_books


# Create your views here.
class BooksList(generic.ListView):
    # queryset = Books.objects.filter(status=1).order_by("-created_on")
    queryset = get_published_books()
    template_name = "books/index.html"
    paginate_by = 6
