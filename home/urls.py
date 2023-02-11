from django.urls import path, include
from . import views as home_views
#from ..blog import views as blog_views
#from .views import UpdatePostView

urlpatterns = [
#     base
    #path("", home_views.Home),
    #path("home/", home_views.Home),
#     blogs
    #path("blog/", include('blog.urls')),
    # path("", views.blogs, name="blogs"),
    # path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    # path("add_blogs/", views.add_blogs, name="add_blogs"),
    # path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    # path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    #path("search/", include('blog.urls'), name="search"),

    
#     profile
    path("profile/", home_views.UserProfile, name="profile"),
    path("edit_profile/", home_views.edit_profile, name="edit_profile"),

#    projects
    path("edit_projects/", home_views.edit_projects, name="edit_projects"),
    # path("user_profile/<int:myid>/", home_views.user_profile, name="user_profile"),
    
#    user authentication
    path("register/", home_views.Register, name="register"),
    path("login/", home_views.Login, name="login"),
    path("logout/", home_views.Logout, name="logout"),

#    search
   # path("search/", include('blog.urls'), name="search"),

    path("", home_views.Home),
]

# https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/#serving-files