from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CoreView(LoginRequiredMixin, TemplateView):
    template_name = "core/core.html"
    login_url = "register"
    
    
    
    
'''
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import WTUserProfileForm
from .models import  WtUser_Profile
# Create your views here.


class ProfileView(LoginRequiredMixin, CreateView):
    model = WtUser_Profile
    form_class = WTUserProfileForm
    template_name = 'core/core.html'
    success_url = reverse_lazy('core')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

'''