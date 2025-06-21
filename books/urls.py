from django.urls import path

from . import views

urlpatterns = [
    path("", views.BooksList.as_view(), name="books"),
    path("archive/", views.BooksArciveList.as_view(), name="books_archive"),
]
