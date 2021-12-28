from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render

from .models import Monster


def list_all(request):
    monsters = Monster.objects.all()
    return render(request, "monsters/list_all.html", {"monsters": monsters})


def details(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)
    return render(request, "monsters/details.html", {"monster": monster})


def edit(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)

    if monster.owner != request.user:
        raise PermissionDenied

    return render(request, "monsters/edit.html", {"monster": monster})


def user_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, "monsters/user_list.html", {"user": user})
