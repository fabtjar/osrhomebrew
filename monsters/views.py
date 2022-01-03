from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render

from .models import Monster


def monster_list(request):
    monsters = Monster.objects.all()
    return render(request, "monsters/list.html", {"monsters": monsters})


def monster_detail(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)
    return render(request, "monsters/detail.html", {"monster": monster})


def monster_edit(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)

    if monster.author != request.user:
        raise PermissionDenied

    return render(request, "monsters/edit.html", {"monster": monster})


def monster_author_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, "monsters/author_list.html", {"user": user})
