from urllib.parse import urlparse


def get_host_referer(request):
    """Return the referer URL if it is of the requested host."""
    referer = request.META.get("HTTP_REFERER")
    if urlparse(referer).netloc == request.get_host():
        return referer
