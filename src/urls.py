from django.contrib import admin
from django.urls import path, include
from base.views import (
    HomeView
)
from django.conf import settings
from .settings import MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name="home"),
    path('api/', include('base.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/posts/', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
