from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse


def profile(request, username):
    author = get_object_or_404(get_user_model(), username=username)

    return TemplateResponse(request, "profile.html", {"author": author})


@login_required
def own_profile(request):
    return profile(request, request.user.username)
