from django.urls import path
from .views import (
    PostListView,
    UserPostsFeedView
)

urlpatterns = [
    path('', PostListView, name="posts-list"),
    path('feed/', UserPostsFeedView, name="user-posts-feed"),
]
