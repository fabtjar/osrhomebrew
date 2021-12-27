from django.urls import path

from .views import details, list_all, user_list


app_name = 'monsters'

urlpatterns = [
    path('', list_all, name='list_all'),
    path('<username>/', user_list, name='user_list'),
    path('<username>/<name>/', details, name='details'),
]
