from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from user_app.models import WTUser
from django.views.generic.edit import CreateView
from .forms import WTUserProfileForm
from .models import WtUser_Profile
from django.urls import reverse_lazy
from post_app.models import WTUserPost

# Create your views here.
class CoreView(LoginRequiredMixin, TemplateView):
    template_name = "core/core.html"
    login_url = "register"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        profile = getattr(self.request.user, 'profile', None)
        
        if profile:
            context['profile_name'] = profile.name
            context['profile_username'] = profile.username
        
        
        context['show_detail_form'] = not getattr(profile, 'profile_completed', False)
    
        if context['show_detail_form']:
            context['form'] = WTUserProfileForm()
            
        return context

class ProfileView(LoginRequiredMixin, CreateView):
    model = WtUser_Profile
    form_class = WTUserProfileForm
    template_name = 'core/core.html'
    success_url = reverse_lazy('core')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile_completed = True
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        context['username'] = user.email 
        context['details'] = WtUser_Profile.objects.get()
        context['posts'] = WTUserPost.objects.all()
        
        return context

    