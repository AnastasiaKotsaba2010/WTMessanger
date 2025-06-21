from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

class RegistrationForm(forms.Form):
    username = forms.EmailField(
        max_length= 255, 
        widget= forms.EmailInput(attrs={'class': 'data-input-img', 'placeholder': "you@example.com"})
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'data-input-img', 'placeholder': "Введи пароль"}),
        label='Пароль'
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'data-input-img', 'placeholder': "Повтори пароль"}),
        label='Підтвердження паролю'
    )

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length= 255, 
        widget= forms.EmailInput(attrs={'class': 'data-input-img', 'placeholder': "you@example.com"})
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'data-input-img', 'placeholder': "Введи пароль"}),
        label='Пароль'
    )
    
    
class CodeVerificationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(1, 7):
            self.fields[f'code_{i}'] = forms.CharField(
                label = '',
                max_length = 1,
                min_length = 1,
                widget = forms.TextInput(attrs = {
                    'class': 'number-code',
                    'placeholder': '__',
                    'maxlength': '1',
                    'autocomplete': 'off'
                })
            )
            
class PersonalInformationForm(forms.Form):
    first_name = forms.CharField(
        max_length= 255,
        widget= forms.EmailInput(attrs={'class': 'data-input-img', 'placeholder': ''})
    )
    last_name = forms.CharField(
        max_length= 255,
        widget= forms.EmailInput(attrs={'class': 'data-input-img', 'placeholder': ''})
    )
    date_of_birth = forms.DateInput()
    username = forms.EmailField(
        max_length= 255, 
        widget= forms.EmailInput(attrs={'class': 'data-input-img', 'placeholder': "you@example.com"})
    )

