from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import UserDetailsForm
from django.contrib.auth.models import User
from user_app.models import Avatar

# # Create your views here.
class CoreView(LoginRequiredMixin ,TemplateView):
    template_name = "core/core.html"
    login_url = 'register' 
    
    def get(self, request: HttpRequest): 
        profile = request.user.profile
        global avatar
        avatar = Avatar.objects.filter(profile = profile, active = True, shown = True).first()       
        
        if request.user.is_authenticated and request.session.get('show_detail_form', False):
            print('show detail form')
            return render(
                request, 
                self.template_name, 
                context= {
                    'form_details': UserDetailsForm(), 
                    'show_detail_form': True,
                    'username': request.user.email,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'avatar': avatar
                })
            
        return render(request, self.template_name)

    def post(self, request: HttpRequest):
        # form = RegistrationForm(request.POST)
        button = request.POST.get('who_send')
        
        if button == 'continue':
            print('continue')
            form = UserDetailsForm(request.POST)
            
            if form.is_valid():
                name = form.cleaned_data['name']
                
                if User.objects.filter(username=name).exclude(pk=request.user.pk).exists():
                    form.add_error('name', 'Користувач з таким ім’ям уже існує')
                    return render(request, self.template_name, {
                        'form_details': form,
                        'show_detail_form': True
                    })

                request.user.first_name = form.cleaned_data['first_name']
                request.user.last_name = form.cleaned_data['last_name']
                request.user.email = name 
                request.user.save()

                request.session.pop('show_detail_form', None)

                return redirect('core') 

            return render(request, self.template_name, {
                'form_details': form,
                'show_detail_form': True,
                'username': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'avatar': avatar
            })
            
        else:
            print('cancel')
            return redirect('core')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     user = self.request.user
    #     profile = getattr(self.request.user, 'profile', None)
        
    #     if profile:
    #         context['profile_name'] = profile.name
    #         context['profile_username'] = profile.username
        
        
    #     context['show_detail_form'] = not getattr(profile, 'profile_completed', False)

            
    #     return context

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
    