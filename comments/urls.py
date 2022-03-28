from .views import (
    CommentListView,
    CommentDetailView
)

from django.urls import path

urlpatterns = [
    path('', CommentListView, name="comments-list"),
    path('<int:id>/', CommentDetailView, name="comments-detail"),
]
