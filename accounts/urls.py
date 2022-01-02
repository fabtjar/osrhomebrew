from django.urls import path

from . import views

urlpatterns = [
    path("email/", views.not_found, name="account_email"),
]
