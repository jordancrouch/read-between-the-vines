from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Provides primary key type for the home app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "home"
