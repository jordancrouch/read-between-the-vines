from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my_books(request):
    return HttpResponse("Hello, books!")
