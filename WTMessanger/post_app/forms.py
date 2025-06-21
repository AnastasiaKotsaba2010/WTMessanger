from django import forms
from .models import Post, Image, Album, Tag, Link


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'topic', 'content', 'tags', 'images']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишіть назву публікації'
            }),
            'topic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишіть тему публікаціїї'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис публікації',
                'id': 'id_content'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                # 'placeholder': 'Оберіть теги'
            }),
            'images': forms.SelectMultiple(attrs={
                'class': 'form-control',
                # 'placeholder': 'Оберіть зображення'
            }),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['filename', 'file']
        widgets = {
            'filename': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва зображення'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control upload-input',
                'id': 'image-upload',
                'name': 'file'
            }),
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'preview_image', 'images', 'shown', 'topic']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва альбому'
            }),
            'preview_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'images': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'shown': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'topic': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва тегу'
            }),
        }


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url', 'post']
        widgets = {
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Посилання'
            }),
            'post': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
