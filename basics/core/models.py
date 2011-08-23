from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from basics.core.managers import BaseManager, CurrentSiteBaseManager
from django.contrib.sites.models import Site


class BaseModel(models.Model):
    is_active = models.BooleanField(verbose_name=_('is active'), default=False, help_text=_("Tick to make this entry live (see also the publication date). Note that administrators (like yourself) are allowed to preview inactive entries whereas the general public aren't."))
    creation_date = models.DateTimeField(verbose_name=_('creation date'), auto_now_add=True, editable=False, null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now, verbose_name=_("publication date"), help_text=_("For an entry to be published, it must be active and its publication date must be in the past."), null=True, blank=True)
    pub_end_date = models.DateTimeField(verbose_name=_("publication end date"), null=True, blank=True)
    last_mod_date = models.DateTimeField(auto_now=True, verbose_name=_("last modification date"), null=True, blank=True)
    order = models.PositiveIntegerField(verbose_name=_('order'), null=True, blank=True)
    #sites = models.ManyToManyField(Site)
    
    user = models.ForeignKey('auth.User', editable=False, verbose_name=_('user'), blank=True, null=True)
    
    objects = BaseManager()
    on_site = CurrentSiteBaseManager()
    
    class Meta:
        abstract = True
        ordering = ('order', '-pub_date', '-creation_date')
        get_latest_by = 'pub_date'