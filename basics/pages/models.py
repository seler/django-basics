from django.db import models
from basics.core.models import BaseModel
from basics.helpers import first_of
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.core.urlresolvers import reverse

PAGE_TYPE_CHOICES = (
    (0, _('page')),
    (1, _('redirect')),
    (2, _('simple')), # only introduction
)
PAGE_TYPE_DEFAULT = 0


class Page(BaseModel):
    title = models.CharField(verbose_name=_('title'), max_length=255, null=True, blank=True)
    slug = models.SlugField(verbose_name=_('slug'), max_length=255, null=True, blank=True)
    url = models.CharField(verbose_name=_('URL'), max_length=255, null=True, blank=True)
    use_url = models.BooleanField(verbose_name=_('use URL'), default=False, help_text=_('Use URL instead of slug'))
    type = models.PositiveIntegerField(verbose_name=_('type'), choices=PAGE_TYPE_CHOICES, default=PAGE_TYPE_DEFAULT, null=True, blank=True)
    category = models.ForeignKey('categories.Category', verbose_name=_('category'), related_name='pages', null=True, blank=True)
    photo = models.ForeignKey('files.Photo', null=True, blank=True, related_name='pages')
    introduction = models.TextField(verbose_name=_('introduction'), blank=True, null=True)
    
    authors = models.ManyToManyField('auth.User', verbose_name=_('authors'), blank=True, null=True, related_name='pages_authors')
    
    enable_comments = models.BooleanField(verbose_name=_('enable comments'), default=False)
    registration_required = models.BooleanField(_('registration required'), default=False, help_text=_("If this is checked, only logged-in users will be able to view the page."))
    
    class Meta:
        db_table = 'basics_pages_page'
        verbose_name_plural = _('page')
        verbose_name_plural = _('pages')

    def __unicode__(self):
        return first_of(self.title, self.slug, self.url)
    
    def get_url(self):
        if self.use_url:
            url = self.url.lstrip('/').rstrip('/')
        else:
            if self.category:
                url = self.category.get_url() + '/' + self.slug
            else:
                url = self.slug
        return url
    path = property(get_url)

#    @models.permalink
    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'path': self.get_url()})
#        return ('pages.views.detail', [self.get_url()])
    
    def is_published(self):
        """
        Return True if the page is publicly accessible.
        """
        return self.is_active and self.pub_date <= datetime.now() and self.pub_end_date > datetime.now()
    is_published.boolean = True
    
#    @property
#    def comments_enabled(self):
#        delta = datetime.datetime.now() - self.pub_date
#        return delta.days < 60

#    def save(self, *args, **kwargs):
#        super(Page, self).save(*args, **kwargs)
