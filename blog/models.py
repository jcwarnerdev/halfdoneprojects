from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django_quill.fields import QuillField
# Create your models here.

class QuillPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    content = QuillField()
    image = models.ImageField(upload_to="blog_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blog')


# class BlogPost(models.Model):
#     title=models.CharField(max_length=255)
#     author= models.ForeignKey(User, on_delete=models.CASCADE)
#     slug=models.CharField(max_length=130)
#     content=models.TextField()
#     image = models.ImageField(upload_to="blog_pics", blank=True, null=True)
#     dateTime=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return str(self.author) +  " Blog Title: " + self.title
    
#     def get_absolute_url(self):
#         return reverse('blogs')
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    blog = models.ForeignKey(QuillPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    
