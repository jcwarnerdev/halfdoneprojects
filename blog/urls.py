
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as blog_views
from .views import UpdatePostView
#from .home import views as home_views
#from .views imporr

urlpatterns = [
    path("add_blogs/", blog_views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", blog_views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", blog_views.search, name="search"),
    path("blog/<str:slug>/", blog_views.blogs_comments, name="blogs_comments"),
    path("", blog_views.blogs, name="blogs"),
    
 #     profile
    #path("profile/", include('home.urls'), name="profile"),
    #path("edit_profile/", include('home.urls'), name="edit_profile"),
    #path("user_profile/<int:myid>/", include('home.urls'), name="user_profile"),
    
#    user authentication
    #path("register/", include('home.urls'), name="register"),
    #path("login/", include('home.urls'), name="login"),
    #path("logout/", include('home.urls'), name="logout"),


# #     profile
#     path("profile/", home_views.Profile, name="profile"),
#     path("edit_profile/", home_views.edit_profile, name="edit_profile"),
#     path("user_profile/<int:myid>/", home_views.user_profile, name="user_profile"),
    
# #    user authentication
#     path("register/", home_views.Register, name="register"),
#     path("login/", home_views.Login, name="login"),
#     path("logout/", home_views.Logout, name="logout"),

    #path('admin/', admin.site.urls),
    #path('home/', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


