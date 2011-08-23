from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example_project.views.home', name='home'),
    
    url(r'^accounts/', include('basics.accounts.urls')),
    
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('basics.pages.urls')),
    url(r'^', include('basics.categories.urls')),
)
