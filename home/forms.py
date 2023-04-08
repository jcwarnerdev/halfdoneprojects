from django import forms
from .models import Profile, Project, About

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_full_name_public', 'user_email_public', 'image', 'image_public', 'bio', 'bio_public', 
    'phone_no', 'phone_no_public', 'facebook', 'facebook_public', 'instagram', 'instagram_public', 
    'linkedin', 'linkedin_public', 'github', 'github_public', 'youtube', 'youtube_public',)
     
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_rank', 'project_name', 'project_link', 'creator', 'project_category', 'project_tags')

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('about',)