from django.urls import path

from . import views

urlpatterns = [
    path("", views.monster_list, name="monsters-monster_list"),
    path("new/", views.monster_create, name="monsters-monster_create"),
    path("<int:monster_id>/", views.monster_detail, name="monsters-monster_detail"),
    path("<int:monster_id>/edit/", views.monster_edit, name="monsters-monster_edit"),
    path(
        "<int:monster_id>/delete/",
        views.monster_delete,
        name="monsters-monster_delete",
    ),
    path("<username>/", views.monster_author_list, name="monsters-monster_author_list"),
]
