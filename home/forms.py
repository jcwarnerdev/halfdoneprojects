from django import forms
from .models import Profile, Project, About

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'github', 'image', )
     
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_rank', 'project_name', 'project_link', 'creator', 'project_category',)

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('about',)