from django.db import models
from basics.core.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from basics.helpers import first_of


class Category(BaseModel):
    parent = models.ForeignKey('self', verbose_name=_('parent'), null=True, blank=True)
    name = models.CharField(verbose_name=_('name'), max_length=255, null=True, blank=True)
    slug = models.SlugField(verbose_name=_('slug'), max_length=255, null=True, blank=True)
    url = models.CharField(verbose_name=_('URL'), max_length=255, null=True, blank=True)
    use_url = models.BooleanField(verbose_name=_('use URL'), default=False, help_text=_('Use URL instead of slug'))
    

    class Meta:
        db_table = 'basics_categories_category'
        verbose_name_plural = _('category')
        verbose_name_plural = _('categories')
    
    def get_url(self):
        if self.use_url:
            url = self.url.lstrip('/').rstrip('/')
        else:
            if self.parent:
                url = self.parent.get_url() + '/' + self.slug
            else:
                url = self.slug
        return url
    path = property(get_url)

    @models.permalink
    def get_absolute_url(self):
        return ('category_detail', {'path': self.get_url()})

    def __unicode__(self):
        return first_of(self.name, self.slug, self.url)