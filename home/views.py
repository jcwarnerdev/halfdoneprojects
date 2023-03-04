from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import Project, Profile, About
from blog.models import QuillPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from .forms import ProfileForm, ProjectForm, AboutForm#, BlogPostForm
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
    about = About.objects.last()
    posts = QuillPost.objects.all()
    posts = QuillPost.objects.filter().order_by('-dateTime')[:3]
    if not posts:
        return redirect("/blog/add_post/")
    # else:
        # return render(request, "blog.html", {'posts':posts})
    return render(request, "home.html", {'about':about, 'posts':posts})

@login_required(login_url = '/login')
def add_about(request):
    if request.user.is_superuser:
        if request.method=="POST":
            form = AboutForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                about = form.save(commit=False)
                about.save()
                # obj = about.instance
                # alert = True
                return redirect("/")
        else:
            form= AboutForm() # BlogPostForm()
        return render(request, "add_about.html", {'form':form})
    else:
        print('not authorized to post')
        form= AboutForm()
        return render(request, "add_about.html", {'form':form})

@login_required(login_url = '/login')
def edit_projects(request):
    # print('edit projects')
    ProjectsFormSet = modelformset_factory(Project, form=ProjectForm, extra=1, can_delete=True)
    # print(ProjectsFormSet)
    if request.method == 'POST' and request.user.is_superuser:
        formset = ProjectsFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        # print('getting formset')
        formset = ProjectsFormSet(queryset=Project.objects.order_by('project_name'))
        # print(formset)
    return render(request, 'edit_projects.html', {'formset': formset})

# @login_required(login_url = '/login')
# def edit_about(request):
#     # print('edit projects')
#     about = About.objects.first()
#     # print(ProjectsFormSet)
#     if request.method == 'POST' and request.user.is_superuser:
#         about = ProjectsFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#     else:
#         # print('getting formset')
#         formset = ProjectsFormSet(queryset=Project.objects.order_by('project_name'))
#         # print(formset)
#     return render(request, 'edit_projects.html', {'formset': formset})

class UpdateAboutView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = About 
    template_name = 'edit_about.html'
    fields = ['id', 'about']
