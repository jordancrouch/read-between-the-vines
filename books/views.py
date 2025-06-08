from django.shortcuts import render
from django.views import generic

from .models import Books


# Create your views here.
class BooksList(generic.ListView):
    queryset = Books.objects.all()
    template_name = "books_list.html"
