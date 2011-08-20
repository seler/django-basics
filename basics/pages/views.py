from django.views.generic import DetailView
from django.http import Http404
from basics.pages.models import Page


class PageDetailView(DetailView):
    queryset = Page.objects.published()
    def get_object(self):
        objects = Page.objects.published()
        try:
            return (object for object in objects if object.path.lstrip('/').rstrip('/') == self.kwargs['path']).next()
        except StopIteration:
            raise Http404