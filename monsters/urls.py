from django.urls import path

from . import views

urlpatterns = [
    path("", views.monster_list, name="monsters-monster_list"),
    path("<int:monster_id>/", views.monster_detail, name="monsters-monster_detail"),
    path("<int:monster_id>/edit/", views.monster_edit, name="monsters-monster_edit"),
    path("<username>/", views.monster_author_list, name="monsters-monster_author_list"),
]
