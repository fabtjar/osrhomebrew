from django.urls import path

from .views import details, list_all


app_name = 'monsters'

urlpatterns = [
    path('', list_all, name='list_all'),
    path('<monster_id>/', details, name='details'),
]
