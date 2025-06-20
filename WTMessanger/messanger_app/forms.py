from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(
        max_length = 255,
        widget = forms.TextInput(attrs={
            'class': 'data-input-img',
            'placeholder': "Повідомлення"
        }   
    ))
    
    attached_image = forms.ImageField(
        widget= forms.ClearableFileInput(attrs={
            'class': 'data-input-img'
        } 
    ))