from base.views import FeedView, PostCreateView
from .api.views import (
    APIBaseView
)

from django.urls import path

urlpatterns = [
    path('api/', APIBaseView, name="api-base"),
    path('feed/', FeedView, name="user-feed"),
    path('create/', PostCreateView, name="post-create"),
]
