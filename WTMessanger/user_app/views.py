from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views import View
from .forms import RegistrationForm, CodeVerificationForm, LoginForm, PersonalInformationForm
from django.contrib.auth.views import LoginView, LogoutView
from core_app.forms import UserDetailsForm
from django.contrib.auth.models import User
from django.http import HttpRequest
from .models import Profile, VerificationCode, Avatar
import random

# Функція генерації випадкового 6-значного коду для підтвердження електронної пошти
def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))
    
# Створюємо клас представлення RegistrationView для відображення сторінки реєстрації
class RegistrationView(View):
    template_name = 'registration/registration.html' # Шлях до шаблону для відображення

    # Коли користувач хоче отримати дані з серверу, відображаємо контексті дані - форму реєстрації
    def get(self, request):
        return render(request=request ,template_name= self.template_name, context={'form': RegistrationForm})

    # Метод обробляє форму та логіку реєстрації, коли користувач реєструється
    def post(self, request: HttpRequest):
        form = RegistrationForm(request.POST) # Ініціалізуємо форму з даними POST
        button = request.POST.get('who_send') # Відслідковуємо, яка кнопка була натиснута

        if button == 'register': # Якщо була натиснута кнопка реєстрації
            if form.is_valid(): # Перевіряємо коректність форми
                
                # Отримуємо введені дані з полів форми: ім'я, пароль та підтвердження паролю
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                password2 = form.cleaned_data['password2']

                # У випадку, якщо паролі співпадають
                if password == password2:
                    # Створюємо нового користувача
                    user_profile = User.objects.create_user(
                        username= username,
                        password= password,
                        email= ''
                    )
                    # # Тимчасово 'деактивуємо' користувача до підтвердження ел.пошти
                    user_profile.is_active = False 

                    code = generate_verification_code() # Генеруємо код підтвердження
                    send_mail(  # Відправляємо код за вказаною електронною поштою
                        subject= 'Код Підтвердження',
                        message= f'Ваш код підтвердження: {code}',
                        recipient_list= [username],
                        from_email= None,
                        fail_silently= False,   
                    )
                    
                    # Створюємо та записуємо в БД код
                    verification_code_form = VerificationCode.objects.create(
                        username = user_profile.username,
                        code= code
                    )
                
                    user_profile.save() # Зберігаємо користувача
                    self.request.session['username'] = username # Зберігаємо логін у сесію
                    # Повертаємо ел.пошту користувача, а також форму
                    return render(request=request ,template_name= self.template_name, context={'email': user_profile.username, 'form_code': CodeVerificationForm})
                else:
                    print('Form is invalid, try again')
        # Якщо була натиснута кнопка для підтвердження ел.пошти
        elif button == 'verification':
            form_code = CodeVerificationForm(request.POST)
            
            if form_code.is_valid():
                # Збираємо код 
                verification_code = ''
                for i in range(6):
                    num = form_code.cleaned_data[f'code_{i+1}']
                    verification_code += num

                # print(verification_code)

                # request.user.username
                
                # Отримуємо логін користувача із сесії
                username = self.request.session['username']
                # Знаходимо код у базі, фільтруємо, щоб код стосувався користувача та отримуємо перше значення
                model_code = VerificationCode.objects.filter(username = username).first()
                
                # Якщо коди співпадають
                if verification_code == model_code.code:
                    # Отримуємо щойно створеного користувача
                    user_profile = User.objects.get(username = username)
                    # 'Активуємо' його профіль
                    user_profile.is_active = True
                    user_profile.save()
                    
                    # Створюємо профіль користувача
                    profile = Profile.objects.create(
                        user = user_profile
                    )

                    # Переходимо на сторінку логіну
                    return redirect('login')
                
        elif button == 'continue':     
            show_detail_form = False   
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                name = form.cleaned_data['email']
                    
                if not User.objects.filter(username=name).exists():
                    user_profile = User.objects.get(username = username)
                    user_profile.first_name = first_name
                    user_profile.last_name = last_name
                    user_profile.email = name
                    user_profile.save()
                    show_detail_form = True
                else:   
                    form.add_error('email', 'Користувач з таким ім’ям вже існує')
                    return render(request=request ,template_name= self.template_name, context={'show_detail_form': show_detail_form, 'form_details': UserDetailsForm})
        return render(request=request ,template_name= self.template_name, context={'form_code': CodeVerificationForm})
    
# Клас представлення для логіну користувача, базується на вбудованому LoginView
class LoginUserView(LoginView):
    template_name = 'login/login.html' # Вказуємо шлях до шаблону з формою авторизації
    authentication_form = LoginForm # Використовуємо кастомну форму для авторизації
    redirect_authenticated_user = True # Якщо користувач вже авторизований — перекидаємо сторінку
    
    # Метод, що виконується після успішної валідації форми
    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.request.user
        # Якщо користувач ще не має імені чи прізвища
        if not user.first_name or not user.last_name:
            #  Вказуємо в сесії, що треба показати форму деталей
            self.request.session['show_detail_form'] = True
        else:
            # В інших випадках форма недоступна
            self.request.session['show_detail_form'] = False

        return response
        
    def get_success_url(self):
        # Перенаправляємо користувача на головну сторінку після успішної авторизації
        return reverse_lazy('core')
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("core")


# friends
class MainFriendsView(View):
    template_name = 'friends/main_friends.html'

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            avatars = profile.avatar_set.filter(active=True, shown=True)
            return render(request, self.template_name, {'avatars': avatars})
        else:
            return redirect('login')

class AllFriendsView(View):
    template_name = 'friends/all_friends.html'

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            friends = profile.friendship_sent_request.filter(accepted=True) | profile.friendship_accepted_request.filter(accepted=True)
            return render(request, self.template_name, {'friends': friends})
        else:
            return redirect('login')
        
class RecommendedFriendsView(View):
    template_name = 'friends/recommendation.html'

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            all_profiles = Profile.objects.exclude(user=request.user)
            friends = profile.friendship_sent_request.filter(accepted=True) | profile.friendship_accepted_request.filter(accepted=True)
            recommended_friends = all_profiles.exclude(id__in=friends.values_list('id', flat=True))
            return render(request, self.template_name, {'recommended_friends': recommended_friends})
        else:
            return redirect('login')
        
class FriendshipRequestView(View):
    template_name = 'friends/requests.html'

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            friendship_requests = profile.friendship_accepted_request.filter(accepted=False)
            return render(request, self.template_name, {'friendship_requests': friendship_requests})
        else:
            return redirect('login')
        
class PersonalInformationView(CreateView):
    template_name = 'settings/settings.html'
    
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            profile = request.user.profile
            avatar = Avatar.objects.filter(profile = profile, active = True, shown = True).first()       
            
            return render(
                request,
                template_name= self.template_name, 
                context= {
                    'username': request.user.email,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'avatar': avatar,
                    'form': PersonalInformationForm
                }
            )
    
    def post(self, request: HttpRequest):
        form = PersonalInformationForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            username = form.cleaned_data['username']
            
            user_profile = request.user.profile
            
            user_profile.date_of_birth = date_of_birth
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.username = username
            user_profile.save()
            
            return redirect('settings')
        
        return render(request, self.template_name, {'form': form})



