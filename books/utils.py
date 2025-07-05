from .models import Books


def get_published_books(category=None, limit=3):
    """
    Utility query function to return published books with the ability to specify a category
    and the number of items to include.
    """
    queryset = Books.objects.filter(status=1).order_by("-updated_on")
    if category:
        queryset = queryset.filter(category__iexact=category)
    return queryset[:limit] if limit else queryset
