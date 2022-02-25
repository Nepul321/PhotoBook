from .views import (
    ProfileListView
)

from django.urls import path

urlpatterns = [
    path('', ProfileListView, name="profiles-list"),
]
