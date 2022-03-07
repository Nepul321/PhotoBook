from .views import (
    ProfileListView,
    ProfileDetailView
)

from django.urls import path

urlpatterns = [
    path('', ProfileListView, name="profiles-list"),
    path('<str:username>/', ProfileDetailView, name="profile-detail"),
]
