from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class Project(models.Model):
    creator = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    project_name = models.CharField(max_length=50, blank=False, null=False)
    project_link = models.URLField(blank=False, null=False)
    project_rank = models.IntegerField(blank=False, null=False)
    project_category = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.project_name)