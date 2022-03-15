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
    UserAccountForm,
    SignUpForm
)

from .models import UserKey
from base.models import User
from src.settings import DEBUG
from src.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

if DEBUG:
    current_host = "http://localhost:8000"
else:
    current_host = ""

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

@unauthenticated_only
def SignUpView(request, *args, **kwargs):
    template = "auth/signup.html"
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            qs = UserKey.objects.filter(user__email=email)
            obj = qs.first()
            subject = "Verify your email"
            message = f"Thanks for signing up. \n Verify your email - {current_host}/accounts/users/{obj.key}/activate/"
            email_from = EMAIL_HOST_USER
            recipient_list = [obj.user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            template = "auth/email_sent.html"
            context = {
                "email" : email
            }

            return render(request, template, context)



    context = {
       'form' : form
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

@login_required
def DeleteAccountView(request, *args, **kwargs):
    template = "auth/delete.html"
    if request.method == "POST":
        user = request.user
        qs = User.objects.filter(id=user.id)
        if not qs:
            return redirect('accounts-account')
        obj = qs.first()
        obj.delete()
        return redirect('/')
    context = {

    }

    return render(request, template, context)

@unauthenticated_only
def AccountVerifyView(request, id, *args, **kwargs):
    template = "auth/email_verify.html"
    context = {

    }
    qs = UserKey.objects.filter(key=id)
    if not qs:
        return redirect('/')

    obj = qs.first()
    if obj.activated == False:
        obj.activated = True
        user = obj.user
        user.is_active = True

        obj.save()
        user.save()

        context = {
             "email" : user.email
        }

        return render(request, template, context)

    return redirect('/')