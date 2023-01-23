from django.contrib import admin
from blog.models import *
from .models import *

admin.site.register(QuillPost)
# admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Profile)