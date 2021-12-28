from django.urls import path

from .views import details, edit, list_all, user_list


app_name = 'monsters'

urlpatterns = [
    path('', list_all, name='list_all'),
    path('<int:monster_id>/', details, name='details'),
    path('<int:monster_id>/edit/', edit, name='edit'),
    path('<username>/', user_list, name='user_list'),
]
