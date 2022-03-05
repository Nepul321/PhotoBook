from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    PostForm
)

from posts.models import Post

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