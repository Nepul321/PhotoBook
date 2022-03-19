from .views import (
    ProfileListView,
    ProfileDetailView,
    UserPostsView
)

from django.urls import path

urlpatterns = [
    path('', ProfileListView, name="profiles-list"),
    path('<str:username>/', ProfileDetailView, name="profile-detail"),
    path('<str:username>/posts/', UserPostsView, name="profile-posts"),
]
