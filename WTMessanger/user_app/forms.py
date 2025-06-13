from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import WTUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'data-input-img', 'placeholder': "Введи пароль"}),
        label='Пароль',
        validators=[validate_password]
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'data-input-img', 'placeholder': "Повтори пароль"}),
        label='Підтвердження паролю'
    )

    class Meta:
        model = WTUser
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'data-input noimg', 'placeholder': "you@example.com"}),
        }
        labels = {
            'email': 'Email',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if WTUser.objects.filter(email=email).exists():
            raise ValidationError("Цей email вже зареєстрований!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error('password2', 'Паролі не співпадають')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].label = "Email"
        self.fields["username"].widget.attrs.update({"class": "data-input noimg", 'placeholder': "you@example.com"})
        self.fields["password"].widget.attrs.update({"class": "data-input-img", 'placeholder': "Введи пароль"})

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise ValidationError("Невірна пошта або пароль")
        return self.cleaned_data




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

    def clean(self):
        cleaned_data = super().clean()
        code_parts = [cleaned_data.get(f'code_{i}') for i in range(1, 7)]
        full_code = ''.join(code_parts)

        if None in code_parts or '' in code_parts:
            raise forms.ValidationError("Усі поля мають бути заповнені")

        if not full_code.isdigit():
            raise forms.ValidationError("Код повинен містити лише цифри")

        cleaned_data['full_code'] = full_code
        return cleaned_data

    
    
    