from .views import (
    CommentListView,
    CommentDetailView,
    PostCommentsView
)

from django.urls import path

urlpatterns = [
    path('', CommentListView, name="comments-list"),
    path('<int:id>/', CommentDetailView, name="comments-detail"),
    path('posts/<int:id>/', PostCommentsView, name="posts-comments-list")
]
