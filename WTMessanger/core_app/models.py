from django.db import models
from user_app.models import WTUser

# Create your models here.
class WtUser_Profile(models.Model):
    user = models.OneToOneField(WTUser, on_delete= models.CASCADE)
    
    name = models.CharField(max_length= 200, null=True)
    last_name = models.CharField(max_length= 200, null=True)
    username = models.CharField(max_length= 200, null=True)
    
    profile_completed = models.BooleanField(default= False)
    
    def __str__(self):
        return self.name
    

class ProfileCard(models.Model):
    user = models.ForeignKey(to= WtUser_Profile, on_delete=models.CASCADE, related_name='profile_card')
    username = models.CharField(max_length=200)
    
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    old_password = models.CharField(max_length=200)
    new_password = models.CharField(max_length=200)