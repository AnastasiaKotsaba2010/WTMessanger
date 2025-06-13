from django.db import models
from user_app.models import WTUser
from core_app.models import WtUser_Profile


# class PostTag(models.Model):
#     tag_name = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.tag_name

# class PostUrl(models.Model):
#     post = models.ForeignKey("WTUserPost", on_delete=models.CASCADE, related_name='links', default= None)
#     url = models.URLField(default= None)

#     def __str__(self):
#         return self.url
class WTUserPost(models.Model):
    author = models.ForeignKey(WtUser_Profile, on_delete=models.CASCADE, related_name='posts')
    
    title = models.CharField(max_length=200)
    
    topic = models.CharField(max_length=200, blank=True, null=True)
    
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

