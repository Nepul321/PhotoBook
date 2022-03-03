from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import (
    unauthenticated_only
)

from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm
)

from django.contrib.auth import (
    login,
    logout,
    update_session_auth_hash
)

from .forms import (
    UserAccountForm
)


@unauthenticated_only
def LoginView(request, *args, **kwargs):
    template = "auth/login.html"
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
       "form": form
    }

    return render(request, template, context)


@login_required
def LogoutView(request, *args, **kwargs):
    logout(request)
    return redirect('accounts-login')


@login_required
def AccountView(request, *args, **kwargs):
    template = "auth/account.html"
    user = request.user
    form = UserAccountForm(instance=user)
    if request.method == "POST":
        form = UserAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts-account')
    context = {
     'form': form
    }

    return render(request, template, context)


@login_required
def PasswordChangeView(request, *args, **kwargs):
    template = "auth/password.html"
    form = PasswordChangeForm(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts-password')

    context = {
       'form' : form
    }

    return render(request, template, context)