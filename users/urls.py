from django.urls import path

from . import views

urlpatterns = [
    path("<username>/", views.profile, name="users-profile"),
    path("", views.own_profile, name="users-own_profile"),
]
