from django import forms
# from .models import BlogPost #Profile,
from django_quill.forms import QuillFormField
from .models import QuillPost

class QuillPostForm(forms.ModelForm):
    class Meta:
        model = QuillPost
        fields = (
            'title', 'slug', 'content', 'image'
        )

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     




# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ('title', 'slug', 'content', 'image')
#         widgets = {
#             'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
#             'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
#             'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
#         }