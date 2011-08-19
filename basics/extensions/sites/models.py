# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class SiteSettings(models.Model):
    site = models.OneToOneField(Site, verbose_name=_('site'), primary_key=True)
    #value = models.CharField(verbose_name=_('value'), max_length=100)

    class Meta:
        db_table = 'basics_site_settings'
        verbose_name = _('site settings')
        verbose_name_plural = _('sites settings')
        ordering = ('site',)
