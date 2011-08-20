# -*- coding: utf-8 -*-
from django.conf import settings

PROJECT_SETTINGS_PREFIX = 'BASICS_'

def get(setting_name, default=None):
    if setting_name in globals():
        default = eval(setting_name)
    return getattr(settings, PROJECT_SETTINGS_PREFIX+setting_name, default)

_ = lambda s: s

FLATPAGES_TEMPLATE_NAME_CHOICES = (
    ('flatpages/default.html', _('Default template')),
    ('flatpages/list.html', _('Flatpages list')),
    ('flatpages/fancy.html', _('Fancy template')),
)

FLATPAGES_TINYMCE_CONFIG = {
    'theme': "advanced",
    'relative_urls': False,
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_blockformats' : "p,address,blockquote,h1,h2,h3,h4,h5,h6,pre,code",
    'theme_advanced_toolbar_align' : "left",
    
}
FLATPAGES_TINYMCE_WIDGET_ATTRS = {
    'cols': 80,
    'rows': 30,
}
