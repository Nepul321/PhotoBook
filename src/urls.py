from django.contrib import admin
from django.urls import path, include
from base.views import (
    HomeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name="home"),
    path('', include('base.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/comments/', include('comments.urls')),
]

