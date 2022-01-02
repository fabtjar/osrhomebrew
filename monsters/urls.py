from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_all, name="monster_list"),
    path("<int:monster_id>/", views.details, name="monster_detail"),
    path("<int:monster_id>/edit/", views.edit, name="monster_edit"),
    path("<username>/", views.author_list, name="monster_author_list"),
]
