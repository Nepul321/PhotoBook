from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    AccountView
)

urlpatterns = [
    path('login/', LoginView, name="accounts-login"),
    path('logout/', LogoutView, name="accounts-logout"),
    path('account/', AccountView, name="accounts-account"),
]
