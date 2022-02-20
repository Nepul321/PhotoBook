from django.urls import path
from .views import (
    PostCreateView,
    PostListView,
    UserPostsFeedView
)

urlpatterns = [
    path('', PostListView, name="posts-list"),
    path('feed/', UserPostsFeedView, name="user-posts-feed"),
    path('create/', PostCreateView , name="posts-create"),
]
