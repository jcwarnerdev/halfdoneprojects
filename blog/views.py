from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import QuillPost, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import QuillPostForm # BlogPostForm #ProfileForm, BlogPostForm
from home.forms import ProfileForm #, BlogPostForm
from django.views.generic import UpdateView
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def blogs(request):
    posts = QuillPost.objects.all() # BlogPost.objects.all()
    posts = QuillPost.objects.filter().order_by('-dateTime')# BlogPost.objects.filter().order_by('-dateTime')
    if not posts:
        # return render(request, "blog.html", {'posts':'testno posts'})
        return redirect("/blog/add_post/")
    else:
        return render(request, "blog.html", {'posts':posts})

@login_required(login_url = '/login')
def search(request):
    print(request.path)
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = QuillPost.objects.filter(title__contains=searched) # BlogPost.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})

# @login_required(login_url = '/login')
def blogs_comments(request, slug):
    print(request.path)
    post = QuillPost.objects.filter(slug=slug).first() # BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method=="POST" and request.path!="/blog/search/":
        print(request.path)
        user = request.user
        content = request.POST.get('content','')
        # blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post':post, 'comments':comments})

@login_required(login_url = '/login')
def Delete_Blog_Post(request, slug):
    posts = QuillPost.objects.get(slug=slug).first() # BlogPost.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', {'posts':posts})

@login_required(login_url = '/login')
def add_post(request):
    if request.method=="POST":
        form = QuillPostForm(data=request.POST, files=request.FILES) # BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            # return render(request, "add_post.html", {'obj':obj, 'alert':alert})
            return redirect("/blog")
    else:
        form= QuillPostForm() # BlogPostForm()
    return render(request, "add_post.html", {'form':form})

# @login_required(login_url = '/login')
# def edit_post(request, slug):
#     # logger.debug(request, slug)
#     # form = QuillPost.objects.filter(slug=slug).first()
#     print(request)
#     # print(request.POST)
#     if request.method=="POST":
#         print('method is post')
#         # print(QuillPost.objects.filter(slug=slug).first().content)
#         # form = QuillPostForm(data=QuillPost.objects.filter(slug=slug).first(), files=request.FILES)
#         form = QuillPostForm(data=request.POST, files=request.FILES)
#         print(form)
#         if form.is_valid():
#             blogpost = form.save(commit=False)
#             blogpost.author = request.user
#             blogpost.save()
#             obj = form.instance
#             alert = True
#             # form = QuillPostForm(data=request.POST, files=request.FILES)
#             # logger.debug(post)
#             # model = QuillPost # BlogPost
#             # template_name = 'edit_blog_post.html'
#             # fields = ['title', 'slug', 'content', 'image']
#             # return render(request, "edit_post.html", {'obj':obj, 'alert':alert})
#             return redirect("/blog")
#         else:
#             print('method is post')
#             form= QuillPostForm(data=request.POST, files=request.FILES) # BlogPostForm()
#             return render(request, "edit_post.html", {'form':form}) 
#     else:
#         print('method is get')
#         # form= QuillPostForm(data=request.POST, files=request.FILES) # BlogPostForm()
#         form = QuillPost.objects.filter(slug=slug).first()
#         print(form)
#         # print(form.instance)
#         return render(request, "edit_post.html", {'form':form}) 


# @login_required(login_url = '/login')
class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = QuillPost 
    template_name = 'edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'image']

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user
                        )

    # def test_func(self):
    #     if self.request.user != self.


# def user_profile(request, myid):
#     post = BlogPost.objects.filter(id=myid)
#     return render(request, "user_profile.html", {'post':post})

# def Profile(request):
#     return render(request, "profile.html")

# def edit_profile(request):
#     try:
#         profile = request.user.profile
#     except Profile.DoesNotExist:
#         profile = Profile(user=request.user)
#     if request.method=="POST":
#         form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             alert = True
#             return render(request, "edit_profile.html", {'alert':alert})
#     else:
#         form=ProfileForm(instance=profile)
#     return render(request, "edit_profile.html", {'form':form})


# def Register(request):
#     if request.method=="POST":   
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
        
#         if password1 != password2:
#             messages.error(request, "Passwords do not match.")
#             return redirect('/register')
        
#         user = User.objects.create_user(username, email, password1)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
#         return render(request, 'login.html')   
#     return render(request, "register.html")

# def Login(request):
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid Credentials")
#         return render(request, 'blog.html')   
#     return render(request, "login.html")

# def Logout(request):
#     logout(request)
#     messages.success(request, "Successfully logged out")
#     return redirect('/login')