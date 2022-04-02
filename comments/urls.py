from .views import (
    CommentListView,
    CommentDetailView,
    PostCommentsView,
    CommentCreateView
)

from django.urls import path

urlpatterns = [
    path('', CommentListView, name="comments-list"),
    path('<int:id>/', CommentDetailView, name="comments-detail"),
    path('posts/<int:id>/', PostCommentsView, name="posts-comments-list"),
    path('posts/<int:post_id>/create/', CommentCreateView, name="comments-create")
]
