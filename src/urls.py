from django.contrib import admin
from django.urls import path, include
from base.views import (
    HomeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name="home"),
    path('api/', include('base.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/posts/', include('posts.urls')),
]
