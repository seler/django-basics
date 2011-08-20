# -*- coding: utf-8 -*-
from django.db import models
from basics import settings
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.views import DEFAULT_TEMPLATE
from django.contrib.sites.models import Site
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

FLATPAGES_TEMPLATE_NAME_CHOICES_DEFAULT = ((DEFAULT_TEMPLATE, _('Default template')),)

class NewFlatPageForm(FlatpageForm):
    sites = forms.ModelMultipleChoiceField(required=True,queryset=Site.objects.all(), widget=forms.widgets.CheckboxSelectMultiple,initial=[Site.objects.get_current()])
    try:
        from tinymce.widgets import TinyMCE
        content = forms.CharField(widget=TinyMCE(attrs=settings.get('FLATPAGES_TINYMCE_WIDGET_ATTRS'), mce_attrs=settings.get('FLATPAGES_TINYMCE_CONFIG')), required=False)
    except ImportError, NameError:
        pass
    template_name = forms.ChoiceField(required=False, label=_('Template'), choices=settings.get('FLATPAGES_TEMPLATE_NAME_CHOICES', FLATPAGES_TEMPLATE_NAME_CHOICES_DEFAULT))
    
    class Meta:
        model = FlatPage

class NewFlatPageAdmin(FlatPageAdmin):
    form = NewFlatPageForm

    # field `sites` moved to `Advanced options`
    fieldsets = FlatPageAdmin.fieldsets
    fieldsets[0][1]['fields'] = list(fieldsets[0][1]['fields'])
    fieldsets[0][1]['fields'].remove('sites')
    fieldsets[1][1]['fields'] = ('sites',) + fieldsets[1][1]['fields']

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, NewFlatPageAdmin)