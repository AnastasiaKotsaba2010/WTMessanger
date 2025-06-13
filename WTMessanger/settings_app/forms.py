from django import forms
from .models import Album, Photo

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'cover', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']