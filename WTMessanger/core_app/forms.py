from django import forms 
from .models import WtUser_Profile, ProfileCard

class WTUserProfileForm(forms.ModelForm):
    class Meta: 
        model = WtUser_Profile
        fields = ['name', 'last_name', 'username']
        
        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'class': 'input-profile',
                    'placeholder': 'Введіть Ваше ім’я', 
                }
            ),
            
            'last_name': forms.TextInput(
                attrs= {
                    'class': 'input-profile',
                    'placeholder': 'Введіть Ваше прізвище'
                }
            ),
            
            'username': forms.TextInput(
                attrs= {
                    'class': 'input-profile',
                    'placeholder': '@'
                }
            )
        }
        
class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = ProfileCard
        fields = ['username', 'name', 'last_name', 'birth_date', 'email', 'old_password', 'new_password']
        widgets = {
            'username': forms.TextInput(
                attrs= {
                    'class': 'input-profile',
                    'placeholder': 'None',
                }
            ),
            'name': forms.TextInput(
                attrs= {
                    'class': 'input-profile',
                    'placeholder': 'None',
                }
            ),
            'last_name': forms.TextInput(
                attrs= {
                    'class': 'input-profile',  
                }
            ),
            'birth_date': forms.DateInput(
                attrs= {
                    'class': 'input-profile',
                    'type': 'date',
                }
            ),
            'email': forms.EmailInput(
                attrs= {
                    'class': 'input-profile',
                    'placeholder': 'None',
                }
            ),
            
            'old_password': forms.PasswordInput(
                attrs= {
                    'class': 'input-profile',   
                    'placeholder': 'Введи старий пароль',   
                }
            ),
            'new_password': forms.PasswordInput(
                attrs= {
                    'class': 'input-profile',
                    'placeholder': 'Введи новий пароль',
                }
            )
        }