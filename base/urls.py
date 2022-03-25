from base.views import (
    FeedView, 
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    ProfileView,
    UpdateProfileView,
    SearchView
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
    path('posts/<int:id>/update/', PostUpdateView, name="post-update"),
    path('u/<str:username>/', ProfileView, name="profile"),
    path('profile/', UpdateProfileView, name="profile-update"),
    path('search/', SearchView, name="search"),
]
