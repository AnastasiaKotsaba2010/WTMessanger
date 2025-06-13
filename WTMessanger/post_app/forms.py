from django import forms
from .models import WTUserPost

class WTUserPostForm(forms.ModelForm):
    class Meta:
        model = WTUserPost
        fields = ['title', 'topic', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'form-control', 
                'placeholder': 'Напишіть назву публікації'
            }),
            'topic': forms.TextInput(attrs= {
                'class': 'form-control', 
                'placeholder': 'Напишіть тему публікаціїї'
            }),
            'content': forms.Textarea(attrs = {
                'class': 'form-control', 
                'placeholder': 'Введіть опис публікації'
            }),
            # 'link': forms.URLInput(attrs= {
            #     'class': 'form-control', 
            #     'placeholder': 'Додайте посилання до публікації'
            # }),
            'image': forms.ClearableFileInput(attrs = {
                'class': 'form-control',
                'id': 'image-upload',
                'class': 'upload-input',
                'name': 'image'
            }),
            # 'tags': forms.SelectMultiple(attrs= {
            #     'class': 'form-control', 
            #     'placeholder': 'Додайте тег до публікації'
            # }),
            
}
