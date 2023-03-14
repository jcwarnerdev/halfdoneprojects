from django.urls import path, include
from . import views as home_views
from .views import UpdateAboutView

urlpatterns = [
   
#     profile
    # path("profile/", home_views.UserProfile, name="profile"),
    # path("profile/<str:user>", home_views.UserProfile, name="profile"),
    path("profile/<int:id>/", home_views.UserProfile, name="profile"),
    path("edit_profile/", home_views.edit_profile, name="edit_profile"),

#    projects
    path("edit_projects/", home_views.edit_projects, name="edit_projects"),
    # path("edit_about/", home_views.edit_about, name="edit_about"),
    path("add_about/", home_views.add_about, name="add_about"),
    path("edit_about/<int:pk>/", UpdateAboutView.as_view(), name="edit_about"),
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