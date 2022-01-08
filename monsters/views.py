from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect

from utils.requests import get_host_referer
from .forms import MonsterForm, SpecialAttackFormSet
from .models import Monster


def monster_list(request):
    paginator = Paginator(Monster.objects.all(), 10)
    page_number = request.GET.get("page")
    monsters = paginator.get_page(page_number)

    return render(request, "monsters/list.html", {"monsters": monsters})


def monster_author_list(request, username):
    author = get_object_or_404(get_user_model(), username=username)

    paginator = Paginator(author.monsters.all(), 10)
    page_number = request.GET.get("page")
    monsters = paginator.get_page(page_number)

    return render(
        request, "monsters/author_list.html", {"author": author, "monsters": monsters}
    )


@login_required
def monster_liked_list(request):
    paginator = Paginator(request.user.liked_monsters.all(), 10)
    page_number = request.GET.get("page")
    monsters = paginator.get_page(page_number)

    return render(request, "monsters/liked_list.html", {"monsters": monsters})


def monster_detail(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)
    return render(request, "monsters/detail.html", {"monster": monster})


def monster_edit(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)

    if monster.author != request.user:
        raise BadRequest("Cannot edit another user's monster.")

    if request.method == "POST":
        form = MonsterForm(request.POST, request.FILES, instance=monster)
        formset = SpecialAttackFormSet(request.POST, instance=monster)
        if form.is_valid() and formset.is_valid():
            monster = form.save()
            formset.save()
            messages.success(request, "Monster updated.")
            return redirect(monster)
    else:
        form = MonsterForm(instance=monster)
        formset = SpecialAttackFormSet(instance=monster)

    return render(
        request,
        "monsters/edit.html",
        {
            "form": form,
            "formset": formset,
        },
    )


@login_required
def monster_create(request):
    if request.method == "POST":
        form = MonsterForm(request.POST, request.FILES)
        if form.is_valid():
            monster = form.save(commit=False)
            formset = SpecialAttackFormSet(request.POST, instance=monster)
            if formset.is_valid():
                monster.author = request.user
                monster.save()
                formset.save()
                messages.success(request, "Monster created.")
                return redirect(monster)
    else:
        form = MonsterForm()
        formset = SpecialAttackFormSet()

    return render(
        request,
        "monsters/create.html",
        {
            "form": form,
            "formset": formset,
        },
    )


def monster_delete(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)

    if monster.author != request.user:
        raise BadRequest("Cannot delete another user's monster.")

    if request.method == "POST":
        monster.delete()
        messages.success(request, "Monster deleted.")
        return redirect("monsters-monster_list")

    return render(request, "monsters/delete.html", {"monster": monster})


@login_required
def monster_like(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)

    referer = get_host_referer(request)

    if request.user.liked_monsters.contains(monster):
        messages.error(request, "Cannot like a monster multiple times.")
        return redirect(referer or monster)

    if request.method == "POST":
        request.user.liked_monsters.add(monster)
        messages.success(request, "Monster liked.")
        return redirect(request.POST.get("referer") or monster)

    return render(
        request,
        "monsters/like.html",
        {
            "monster": monster,
            "referer": referer,
        },
    )


@login_required
def monster_unlike(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)

    referer = get_host_referer(request)

    if not request.user.liked_monsters.contains(monster):
        messages.error(request, "Can only unlike monsters you already like.")
        return redirect(referer or monster)

    if request.method == "POST":
        request.user.liked_monsters.remove(monster)
        messages.success(request, "Monster unliked.")
        return redirect(request.POST.get("referer") or monster)

    return render(
        request,
        "monsters/unlike.html",
        {
            "monster": monster,
            "referer": referer,
        },
    )
