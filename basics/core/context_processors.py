from basics import settings
from django.contrib.sites.models import Site

def utils(request):
    """
    Passes some useful constants.
    """
    return {'site': Site.objects.get_current(),
            'MEDIA_URL': settings.get('MEDIA_URL'),
            'STATIC_URL': settings.get('STATIC_URL'),
            }