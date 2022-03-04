from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import (
    PostForm
)

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
      'form' : form
    }

    return render(request, template, context)