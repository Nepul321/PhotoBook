from django import forms
from django.contrib.auth.forms import (
    UserChangeForm
)

from base.models import User

class UserAccountForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'email')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'})
        }