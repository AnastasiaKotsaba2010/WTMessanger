from django import forms 
from .models import WtUser_Profile

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