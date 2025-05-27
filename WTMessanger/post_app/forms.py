from django import forms
from .models import WTUser_Post

class WTUserPostForm(forms.ModelForm):
    class Meta:
        model = WTUser_Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'form-control', 
                'placeholder': 'Заголовок поста'
            }),
            'content': forms.Textarea(attrs = {
                'class': 'form-control', 
                'placeholder': 'Текст публікації'
            }),
            'image': forms.ClearableFileInput(attrs = {
                'class': 'form-control'
            }),
        }
