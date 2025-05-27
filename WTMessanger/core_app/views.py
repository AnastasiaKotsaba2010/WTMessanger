from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CoreView(LoginRequiredMixin, TemplateView):
    template_name = "core/core.html"
    login_url = "register"