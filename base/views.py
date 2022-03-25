from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    PostForm,
    ProfileForm
)

from posts.models import Post
from profiles.models import Profile

def HomeView(request, *args, **kwargs):
    template = "base/home.html"
    context = {

    }

    return render(request, template, context)

@login_required
def FeedView(request, *args, **kwargs):
    template = "posts/feed.html"
    context = {

    }

    return render(request, template, context)

@login_required
def PostCreateView(request, *args, **kwargs):
    template = "posts/create.html"
    form = PostForm()
    context = {
      'form' : form,
    }

    return render(request, template, context)

@login_required
def PostUpdateView(request, id, *args, **kwargs):
    template = "posts/update.html"
    qs = Post.objects.filter(id=id)
    if not qs:
        return redirect('user-feed')

    obj = qs.first()
    if obj.user != request.user:
        return redirect('user-feed')
    form = PostForm(instance=obj)
    context = {
      'form' : form,
      'obj' : obj
    }

    return render(request, template, context)

def PostDetailView(request, *args, **kwargs):
    template = "posts/details.html"
    context = {

    }

    return render(request, template, context)

def ProfileView(request, *args, **kwargs):
    template = "profiles/profile.html"
    context = {

    }

    return render(request, template, context)

@login_required
def UpdateProfileView(request, *args, **kwargs):
    template = "profiles/update.html"
    user = request.user
    qs = Profile.objects.filter(user=user)
    obj = qs.first()
    form = ProfileForm(instance=obj)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('profile-update')

    context = {
      'form' : form,
      'obj' : obj
    }

    return render(request, template, context)

def SearchView(request, *args, **kwargs):
    template = "posts/search.html"
    context = {

    }

    return render(request, template, context)