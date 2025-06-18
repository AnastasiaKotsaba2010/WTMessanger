from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
import random, string 
from django.http import HttpRequest
from .models import Profile
# Create your views here.


class RegistrationView(View):
    
    template_name = 'registration/registration.html'


    def get(self, request):
        return render(request=request ,template_name= self.template_name, context={'form': RegistrationForm})
    
    def post(self, request: HttpRequest):
        form = RegistrationForm(request.POST)
    
        if form.is_valid():
        
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password == password2:
                user_profile = User.objects.create_user(
                    username= username,
                    password= password,
                    email= ''
                )
                # user_profile.is_active = False 
                
                profile = Profile.objects.create(
                    user = user_profile
                )
                user_profile.save()
            else:

                pass
                # user_profile.save()
        
        return render(request=request ,template_name= self.template_name, context={'form': RegistrationForm})
    


class LoginUserView(LoginView):
    template_name = 'login/login.html'
    # authentication_form = LoginForm
    redirect_authenticated_user = True
    next_page = reverse_lazy('core')



class UserLogoutView(LogoutView):
    next_page = reverse_lazy("core")


class CodeVerificationView(FormView):
    template_name = 'registration/auntification_code.html'
    # form_class = CodeVerificationForm
    success_url = reverse_lazy('core')
    
    def dispatch(self, request, *args, **kwargs):
        if 'registration_data' not in request.session:
            return redirect('register')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user_code = form.cleaned_data['full_code']
        saved_code = self.request.session.get('verification_code')
        
        if user_code != saved_code:
            for field in ['code_1', 'code_2', 'code_3', 'code_4', 'code_5', 'code_6']:
                form.add_error(field, '')
            form.add_error(None, 'Невірний код підтвердження')
            return self.form_invalid(form)
        
        registration_data = self.request.session['registration_data']
        # user = WTUser.objects.create_user(
        #     email = registration_data['email'],
        #     password = registration_data['password']
        # )
        
        # login(self.request, user)
        
        for key in ['registration_data', 'verification_code']:
            if key in self.request.session:
                del self.request.session[key]
        
        messages.success(self.request, 'Реєстрація успішно завершена!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = self.request.session['registration_data']['email']
        context['code_range'] = range(1, 7)
        return context


