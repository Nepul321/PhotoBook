from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    AccountView,
    PasswordChangeView,
    DeleteAccountView
)

urlpatterns = [
    path('login/', LoginView, name="accounts-login"),
    path('logout/', LogoutView, name="accounts-logout"),
    path('account/', AccountView, name="accounts-account"),
    path('password/', PasswordChangeView, name="accounts-password"),
    path('delete/', DeleteAccountView, name="accounts-delete"),
]
