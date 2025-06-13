from django.db import models
from user_app.models import WTUser

# Create your models here.
class WtUser_Profile(models.Model):
    user = models.OneToOneField(WTUser, on_delete= models.CASCADE, related_name= 'profile')
    
    name = models.CharField(max_length= 200, null=True)
    last_name = models.CharField(max_length= 200, null=True)
    username = models.CharField(max_length= 200, null=True)
    
    profile_completed = models.BooleanField(default= False)
    
    def __str__(self):
        return self.name