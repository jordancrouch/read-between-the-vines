from django.views.generic import TemplateView


# Create your views here.
class Homepage(TemplateView):
    template_name = "home/index.html"
