from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify
from django_quill.fields import QuillField

class QuillPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    content = QuillField()
    image = models.ImageField(upload_to="blog_pics", blank=True, null=True)
    # dateTime = models.DateTimeField(auto_now_add=True)
    publish_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    # def save(self, *args, **kwargs):
    #     # if self.slug is None:
    #     #     self.slug = slugify(self.title)
    #     super.save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f"/blog/blog/{self.slug}"

    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(QuillPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    

def slugify_instance_title(instance, new_slug=None):
    if new_slug is not None:
        print(f'new proposed slug: {new_slug}')
        slug = new_slug
    else:
        slug = slugify(instance.title[:100])
        print(f'proposed slug from title: {slug}')
    qs = QuillPost.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        if len(slug) > 95:
              slug = f'{instance.slug[:-5]}-{str(qs.count() + 1)}'
        else:
             slug = f'{instance.slug}-{str(qs.count() + 1)}'
        return slugify_instance_title(instance, new_slug=slug)
    instance.slug = slug
    return instance


def quillpost_pre_save(sender, instance, *args, **kwargs):
    print('quillpost_pre_save')
    print(instance)
    
    instance = slugify_instance_title(instance)
    if instance.slug is None:
            instance.slug = slugify(instance.title[:100])
    qs = QuillPost.objects.filter(slug=instance.slug).exclude(id=instance.id)
    if qs.exists():
        if len(instance.slug) > 95:
              instance.slug = f'{instance.slug[:-5]}-{str(qs.count() + 1)}'
        else:
             instance.slug = f'{instance.slug}-{str(qs.count() + 1)}'
        return
    pass

pre_save.connect(quillpost_pre_save, sender=QuillPost)