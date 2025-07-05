from django.apps import AppConfig


class BooksConfig(AppConfig):
    """
    Provides primary key type for the books app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "books"
