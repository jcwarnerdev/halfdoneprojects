
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as blog_views
from .views import UpdatePostView

app_name = 'blog'
urlpatterns = [
    path("add_post/", blog_views.add_post, name="add_post"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("edit_post/<str:slug>/", UpdatePostView.as_view(), name="edit_post"),
    path("delete_blog_post/<str:slug>/", blog_views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", blog_views.search, name="search"),
    path("blog/<str:slug>/", blog_views.blogs_comments, name="blogs_comments"),
    path("", blog_views.blogs, name="blog"),
] 

# https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/#serving-files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


