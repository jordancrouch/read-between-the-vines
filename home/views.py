from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from books.models import Books
from books.utils import get_published_books


class Homepage(TemplateView):
    """
    View for displaying the homepage.

    Attributes:
        template_name (str): the template used to render the homepage.
    """

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        currently_reading_books = get_published_books(category="CR")
        for book in currently_reading_books:
            avg = book.progress.aggregate(avg=Avg("percentage"))["avg"] or 0
            book.avg_progress = round(avg)

        to_be_read_books = get_published_books(category="TBR")

        context["currently_reading_books"] = currently_reading_books
        context["to_be_read_books"] = to_be_read_books
        context["contact_url"] = reverse_lazy("contact")

        return context
