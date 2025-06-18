from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from user_app.models import WTUser
# from django.views.generic.edit import CreateView
# from .forms import WTUserProfileForm, PersonalInformationForm
# from .models import WtUser_Profile, ProfileCard
# from django.urls import reverse_lazy
# # from post_app.models import WTUserPost
# from django.views.generic.edit import FormView

# # Create your views here.
class CoreView(TemplateView):
    template_name = "core/core.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        profile = getattr(self.request.user, 'profile', None)
        
        if profile:
            context['profile_name'] = profile.name
            context['profile_username'] = profile.username
        
        
        context['show_detail_form'] = not getattr(profile, 'profile_completed', False)

            
        return context

# class ProfileView(LoginRequiredMixin, CreateView):
#     model = WtUser_Profile
#     form_class = WTUserProfileForm
#     template_name = 'core/core.html'
#     success_url = reverse_lazy('core')
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.profile_completed = True
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         user = self.request.user
#         context['username'] = user.email 
#         context['details'] = WtUser_Profile.objects.get()
#         # context['posts'] = WTUserPost.objects.all()
        
#         return context

    
# class SettingsView(FormView):
#     template_name = 'settings/settings.html'
#     form_class = PersonalInformationForm
#     success_url = reverse_lazy('core')
    
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['users'] = self.request.user
#         return kwargs

#     def form_valid(self, form):
#         user_profile = WtUser_Profile.objects.get(user=self.request.user)
#         user_profile.name = form.cleaned_data['name']
#         user_profile.last_name = form.cleaned_data['last_name']
#         user_profile.username = form.cleaned_data['username']
#         user_profile.save()
#         profile_card = ProfileCard.objects.get(user=user_profile)
#         profile_card.username = form.cleaned_data['username']
#         profile_card.name = form.cleaned_data['name']
#         profile_card.last_name = form.cleaned_data['last_name']
#         profile_card.birth_date = form.cleaned_data['birth_date']
#         profile_card.email = form.cleaned_data['email']

#         if form.cleaned_data['old_password'] and form.cleaned_data['new_password']:
#             if not self.request.user.check_password(form.cleaned_data['old_password']):
#                 form.add_error('old_password', 'Невірний старий пароль')
#             else:
#                 self.request.user.set_password(form.cleaned_data['new_password'])
#                 self.request.user.save()
#         profile_card.save()
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_profile = WtUser_Profile.objects.get(user=self.request.user)
#         context['profile'] = user_profile
#         context['profile_card'] = ProfileCard.objects.get(user=user_profile)
#         context['form'] = self.get_form()
#         return context
    