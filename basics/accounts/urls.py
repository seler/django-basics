from django.conf.urls.defaults import *
from basics.accounts.views import UserProfileDetail, SelfUserProfileDetail
#from registration.forms import RegistrationFormUniqueEmail

urlpatterns = patterns('',
    #FIXME: consider moving this to separate module so developers can decide whether they want to use them or not (and templates too)
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^logout/then/login/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^password/change/$', 'django.contrib.auth.views.password_change'),
    url(r'^password/change/done/$', 'django.contrib.auth.views.password_change_done'),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset'),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name='auth_password_reset_done'),
    url(r'^password/reset/confirm/$', 'django.contrib.auth.views.password_reset_confirm', name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='auth_password_reset_complete'),
    
    url(r'^profile/$', SelfUserProfileDetail.as_view(), name='accounts_self_user_profile'),
    url(r'^profile/(?P<username>\w+)/$', UserProfileDetail.as_view(), name='accounts_user_profile'),

)
