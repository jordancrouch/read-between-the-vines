from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Books, Comment, ReadingProgress


class ReadingProgressInline(admin.TabularInline):
    """
    Inline admin interface for the ReadingProgress model.

    Displays reading progress entries in a tabular format within the books
    model admin page. Allows editing of existing progress and adding new entries.

    Attributes:
        model (Model): the ReadingProgress model to inline.
        extra (int): the number of empty forms displayed by default (1).
        fields (tuple): the fields to display in the inline form.
        readonly_fields (tuple): fields that are read-only in the admin interface.
        show_link_change (bool): whether to display a link to edit the related object.

    """

    model = ReadingProgress
    extra = 1
    fields = ("user", "percentage", "created_on", "updated_on")
    readonly_fields = ("created_on", "updated_on")
    show_change_link = True


@admin.register(Books)
class BooksAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Books model, using Summernote's rich text editor.

    Provides additional functionality in the admin interface for managing book entries,
    including search, filtering, inline reading progress editing, and automatic slug generation.

    Attributes:
        list_display (tuple): the fields to display in the list view.
        search_fields (list): the fields that can be searched in the admin search.
        list_filter (tuple): the fields that can be used to filter the entries list.
        prepopulated_fields (dict): prepopulate the slug using the entry title.
        summernote_fields (tuple): the field(s) to use Summernote's rich text editor with.
        inlines (list): include inline editing of ReadingProgress for each book.

    """

    list_display = ("title", "slug", "category", "status")
    search_fields = ["title", "content"]
    list_filter = ("category", "status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
    inlines = [ReadingProgressInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.

    Provides basic functionality to manage user comments in the admin area.
    """

    pass
