from django.db import models
from user_app.models import Profile


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    
    topic = models.CharField(max_length=200) # нове поле
    
    content = models.TextField(max_length=4096)
    images = models.ManyToManyField('Image', blank=True, related_name='posts_authored')
    views = models.ManyToManyField(Profile, blank=True, related_name='posts_viewed')
    likes = models.ManyToManyField(Profile, blank=True, related_name='posts_liked')
    tags = models.ManyToManyField('Tag', blank=True)

    def str(self):
        return self.title


class Image(models.Model):
    filename = models.CharField(max_length=150)
    file = models.ImageField(upload_to='images/posts')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.filename
    

class Album(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to='images/album_previews', null=True, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    shown = models.BooleanField(default=True) 
    topic = models.ForeignKey('Tag', on_delete=models.CASCADE)

    def str(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, default=None)

    def str(self):
        return self.name
    

class Link(models.Model):
    url = models.URLField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def str(self):
        return f'Посилання для поста "{self.post}"'