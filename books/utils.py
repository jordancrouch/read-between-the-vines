from .models import Books


def get_published_books(category=None):
    queryset = Books.objects.filter(status=1).order_by("-created_on")
    if category:
        queryset = queryset.filter(category__iexact=category)
    return queryset
