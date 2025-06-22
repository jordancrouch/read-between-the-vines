from django.urls import path

from books.views import ContactView

from . import views

urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
]
