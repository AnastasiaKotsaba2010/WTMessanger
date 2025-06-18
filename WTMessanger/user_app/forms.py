from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length= 50)
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'data-input-img', 'placeholder': "Введи пароль"}),
        label='Пароль'
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'data-input-img', 'placeholder': "Повтори пароль"}),
        label='Підтвердження паролю'
    )

