from .models import Books


def get_published_books(category=None, limit=3):
    queryset = Books.objects.filter(status=1).order_by("-updated_on")
    if category:
        queryset = queryset.filter(category__iexact=category)
    return queryset[:limit] if limit else queryset
