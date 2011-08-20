from django.conf.urls.defaults import patterns, url
from basics.categories.views import CategoryDetailView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)/$', CategoryDetailView.as_view(), {}, 'category_detail'),
)

