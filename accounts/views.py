from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import (
    unauthenticated_only
)

@unauthenticated_only
def LoginView(request, *args, **kwargs):
    template = "auth/login.html"
    context = {

    }

    return render(request, template, context)

@login_required
def LogoutView(request, *args, **kwargs):
    return redirect('/')