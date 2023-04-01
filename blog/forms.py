from django import forms
from django_quill.forms import QuillFormField
from .models import QuillPost

class QuillPostForm(forms.ModelForm):
    class Meta:
        model = QuillPost
        fields = (
            'title', 'image', 'content', 
        )