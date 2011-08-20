from basics.categories.views import category
from django.http import Http404
from django.conf import settings

class CategoryFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response # No need to check for a flatpage for non-404 responses.
        try:
            return category(request, request.path_info)
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
