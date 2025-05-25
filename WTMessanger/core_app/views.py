from django.views.generic import TemplateView


# Create your views here.
class CoreView(TemplateView):
    template_name = "core/core.html"
