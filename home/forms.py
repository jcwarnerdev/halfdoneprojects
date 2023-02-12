from django import forms
from .models import Profile, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_rank', 'project_name', 'project_link', 'creator', 'project_category')