from base.views import (
    FeedView, 
    PostCreateView,
    PostDetailView
)
from .api.views import (
    APIBaseView
)

from django.urls import path

urlpatterns = [
    path('api/', APIBaseView, name="api-base"),
    path('feed/', FeedView, name="user-feed"),
    path('create/', PostCreateView, name="post-create"),
    path('posts/<int:id>/', PostDetailView, name="post-detail"),
]
