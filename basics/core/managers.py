from django.db import models
from datetime import datetime
from django.conf import settings


class BaseManager(models.Manager):
    
    def published(self):
#        return super(BaseManager, self).get_query_set().filter(sites__id__exact=settings.SITE_ID, is_active=True, pub_date__lte=datetime.now(), pub_end_date__gt=datetime.now())
        return super(BaseManager, self).get_query_set().filter(sites__id__exact=settings.SITE_ID, is_active=True, pub_date__lte=datetime.now())
    
    def all(self):
        return super(BaseManager, self).get_query_set().filter(sites__id__exact=settings.SITE_ID)