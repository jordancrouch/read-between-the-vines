app_name = "books"
from django.urls import path

from . import views

urlpatterns = [
    path("", views.BooksList.as_view(), name="books"),
    path("archive/", views.BooksArciveList.as_view(), name="books_archive"),
    path("<slug:slug>/", views.BookDetail.as_view(), name="book_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.CommentEditView.as_view(),
        name="comment_edit",
    ),
]
