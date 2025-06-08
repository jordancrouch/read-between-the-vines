from django import forms
from django.contrib import admin

from .models import Books, Comment


# Register your models here.
class BooksAdminForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"id": "ckeditor-content"}),
        }

    class Media:
        js = (
            "https://cdn.ckeditor.com/ckeditor5/45.2.0/ckeditor5.umd.js",  # Load CKEditor from CDN
            "js/ckeditor-init.js",  # Custom init script
        )
        css = {
            "all": (
                "css/ckeditor-admin.css",
                "https://cdn.ckeditor.com/ckeditor5/45.2.0/ckeditor5.css",
            )
        }


class BooksAdmin(admin.ModelAdmin):
    form = BooksAdminForm


admin.site.register(Books, BooksAdmin)
admin.site.register(Comment)
