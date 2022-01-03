from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect

from .forms import MonsterForm
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

    if request.method == "POST":
        form = MonsterForm(request.POST, instance=monster)
        if form.is_valid():
            monster = form.save()
            messages.success(request, "Monster updated.")
            return redirect(monster)
    else:
        form = MonsterForm(instance=monster)

    return render(request, "monsters/edit.html", {"monster": monster, "form": form})


def monster_author_list(request, username):
    author = get_object_or_404(get_user_model(), username=username)
    return render(request, "monsters/author_list.html", {"author": author})


def monster_create(request):
    if request.method == "POST":
        form = MonsterForm(request.POST, request.FILES)
        if form.is_valid():
            monster = form.save(commit=False)
            monster.author = request.user
            monster.save()
            messages.success(request, "Monster created.")
            return redirect(monster)
    else:
        form = MonsterForm()

    return render(request, "monsters/edit.html", {"form": form})
