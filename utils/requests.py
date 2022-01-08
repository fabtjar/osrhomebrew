from urllib.parse import urlparse

from django.conf import settings
from django.urls import reverse


def get_host_referer(request):
    """Return the referer URL if it is of the requested host."""
    referer = request.META.get("HTTP_REFERER")

    parsed_url = urlparse(referer)

    if parsed_url.path == reverse(settings.LOGIN_URL):
        return

    if parsed_url.netloc == request.get_host():
        return referer
