from django.urls import path
from .views import (
    PostCreateView,
    PostListView,
    UserPostsFeedView,
    PostDetailView,
    PostLikeUnlikeView,
    PostDeleteView,
    PostUpdateView,
    PostGlobalView
)

urlpatterns = [
    path('', PostListView, name="posts-list"),
    path('feed/', UserPostsFeedView, name="user-posts-feed"),
    path('create/', PostCreateView , name="posts-create"),
    path('<int:id>/',  PostDetailView, name="post-details"),
    path('action/', PostLikeUnlikeView, name="post-like-unlike"),
    path('<int:id>/delete/', PostDeleteView, name="post-delete"),
    path('<int:id>/update/', PostUpdateView, name="post-update"),
    path('global/', PostGlobalView, name="posts-global")
]
