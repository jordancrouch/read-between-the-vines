from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Books, Comment, ReadingProgress


class ReadingProgressInline(admin.TabularInline):
    model = ReadingProgress
    extra = 1
    fields = ("user", "percentage", "created_on", "updated_on")
    readonly_fields = ("created_on", "updated_on")
    show_change_link = True


# Register your models here.
@admin.register(Books)
class BooksAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "category", "status")
    search_fields = ["title", "content"]
    list_filter = ("category", "status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
    inlines = [ReadingProgressInline]


admin.site.register(Comment)
