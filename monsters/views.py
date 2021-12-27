from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from .models import Monster


def list_all(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/list_all.html', {'monsters': monsters})


def details(request, username, name):
    monster = get_object_or_404(Monster, owner__username=username, name=name)
    return render(request, 'monsters/details.html', {'monster': monster})


def user_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'monsters/user_list.html', {'user': user})
