from django.conf.urls.defaults import patterns, url
from basics.pages.views import PageDetailView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)/$', PageDetailView.as_view(), {}, 'page_detail'),
)

