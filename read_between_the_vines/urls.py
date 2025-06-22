"""
URL configuration for read_between_the_vines project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import include, path


def trigger_404(request):
    return render(request, "404.html", status=404)


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls"), name="home-urls"),
    path("books/", include("books.urls", namespace="books"), name="books-urls"),
    path("404/", trigger_404),
]
