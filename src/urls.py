from django.contrib import admin
from django.urls import path, include
from base.views import (
    HomeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name="home"),
    path('api/', include('base.urls')),
]
