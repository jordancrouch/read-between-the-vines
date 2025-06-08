from django.urls import path

from . import views

urlpatterns = [
    path("", views.BooksList.as_view(), name="books"),
]
