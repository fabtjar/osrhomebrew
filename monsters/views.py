from django.shortcuts import render, get_object_or_404

from .models import Monster


def list_all(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/list_all.html', {'monsters': monsters})


def details(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)
    return render(request, 'monsters/details.html', {'monster': monster})
