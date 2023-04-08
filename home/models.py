from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from taggit.managers import TaggableManager

def json_default_vals():
    return

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    user_full_name_public = models.BooleanField(default=False)
    user_email_public = models.BooleanField(default=False)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    image_public = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    bio_public = models.BooleanField(default=False)
    phone_no = models.IntegerField(blank=True, null=True)
    phone_no_public = models.BooleanField(default=False)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    facebook_public = models.BooleanField(default=False)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    instagram_public = models.BooleanField(default=False)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    linkedin_public = models.BooleanField(default=False)
    github = models.CharField(max_length=300, blank=True, null=True)
    github_public = models.BooleanField(default=False)
    youtube = models.CharField(max_length=300, blank=True, null=True)
    youtube_public = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    project_name = models.CharField(max_length=50, blank=False, null=False, default='', unique=True)
    project_link = models.URLField(blank=False, null=False, default='')
    project_rank = models.IntegerField(blank=False, null=False, default=0)
    project_category = models.CharField(max_length=50, blank=False, null=False, default='')
    project_tags = TaggableManager()

    def __str__(self):
        return str(self.project_name)

class About(models.Model):
    about = QuillField()