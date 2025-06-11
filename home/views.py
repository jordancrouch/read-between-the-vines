from django.views.generic import TemplateView

from books.utils import get_published_books


# Create your views here.
class Homepage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["currently_reading_books"] = get_published_books(category="CR")
        context["to_be_read_books"] = get_published_books(category="TBR")

        return context
