from django.shortcuts import render
from django.views import generic

from .models import Books


# Create your views here.
class BooksList(generic.ListView):
    queryset = Books.objects.filter(category="FR", status=1).order_by("-created_on")
    template_name = "books_list.html"
