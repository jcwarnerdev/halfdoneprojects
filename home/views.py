from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm #, BlogPostForm
# from blog.forms import BlogPostForm #ProfileForm, 
from django.views.generic import UpdateView
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


# def user_profile(request, myid):
#     post = BlogPost.objects.filter(id=myid)
#     return render(request, "user_profile.html", {'post':post})

def UserProfile(request):
    return render(request, "profile.html")

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # profile = Profile(user=request.user)
        Profile.objects.create(user=request.user)
    if request.method=="POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "edit_profile.html", {'alert':alert})
    else:
        form=ProfileForm(instance=profile)
    return render(request, "edit_profile.html", {'form':form})


def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        Profile.objects.create(user=user)
        return render(request, 'login.html')   
    return render(request, "register.html")

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        logger.debug(f'{username} is trying to login')
        user = authenticate(request, username=username, password=password)
        logger.debug(f'user info {user}')

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            logger.debug(f'{user} successfully logged in')
            return redirect("/blog")
            # return redirect("/")
            #return render(request, "login.html")
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, "login.html")   
    return render(request, "login.html")

def Logout(request):
    logout(request)
    #messages.success(request, "Successfully logged out")
    return redirect('/login')

def Home(request):
    logger.debug(request)
    return render(request, "home.html")