from django.conf.urls.defaults import *
from basics.accounts.views import UserProfile, UserProfileDetail
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
    
    url(r'^profile/$', UserProfile.as_view(), name='accounts_user_profile_detail'),
    
    
#    url(
#        r'^register/$', 
#        "registration.views.register", 
#        {'form_class': RegistrationFormUniqueEmail},
#        name='registration_register',
#    ),
#    url(
#        r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
#        'django.contrib.auth.views.password_reset_confirm',
#        name='auth_password_reset_confim',
#    ),
#    url(
#        r'^reset/done/$', 
#        'django.contrib.auth.views.password_reset_complete'
#    ),
#    (r'', include('registration.urls')),
)
