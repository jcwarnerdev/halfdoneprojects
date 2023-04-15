from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import QuillPost, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import QuillPostForm
from home.forms import ProfileForm 
from django.views.generic import UpdateView
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def blogs(request):
    posts = QuillPost.objects.all()
    posts = QuillPost.objects.filter().order_by('-publish_dt')
    if not posts:
        return redirect("/blog/add_post/")
    else:
        return render(request, "blog.html", {'posts':posts})

# @login_required(login_url = '/login')
def search(request):
    print(request.path)
    if request.method == "POST":
        searched = request.POST['searched']
        posts = QuillPost.objects.filter(Q(title__icontains=searched) | Q(content__icontains=searched))
        return render(request, "search.html", {'searched':searched, 'posts':posts})
    else:
        return render(request, "search.html", {})

# @login_required(login_url = '/login')
def blogs_comments(request, slug):
    print(request.path)
    post = QuillPost.objects.filter(slug=slug).first()
    if post != None:
        comments = Comment.objects.filter(blog=post)
        if request.method=="POST" and request.path!="/blog/search/":
            print(request.path)
            user = request.user
            content = request.POST.get('content','')
            comment = Comment(user = user, content = content, blog=post)
            comment.save()
        return render(request, "blog_comments.html", {'post':post, 'comments':comments})
    else:
        return redirect('/')

@login_required(login_url = '/login')
def Delete_Blog_Post(request, slug):
    posts = QuillPost.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', {'posts':posts})

@login_required(login_url = '/login')
def add_post(request):
    if request.user.is_superuser:
        if request.method=="POST":
            form = QuillPostForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                blogpost = form.save(commit=False)
                blogpost.author = request.user
                blogpost.save()
                form.save_m2m()
                obj = form.instance
                alert = True
                return redirect("/blog")
        else:
            form= QuillPostForm() # BlogPostForm()
        return render(request, "add_post.html", {'form':form})
    else:
        print('not authorized to post')
        form= QuillPostForm()
        return render(request, "add_post.html", {'form':form})

# @login_required(login_url = '/login')
class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = QuillPost 
    template_name = 'edit_blog_post.html'
    fields = ['title', 'image', 'content', 'tags']

    # def get_queryset(self, *args, **kwargs):
    #     return super().get_queryset(*args, **kwargs).filter(
    #         author=self.request.user
    #                     )

