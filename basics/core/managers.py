from django.db import models
from datetime import datetime
from django.contrib.sites.managers import CurrentSiteManager

Q = models.Q
NOW = datetime.now()

class BaseManager(models.Manager):
    '''Be sure to always use ``published`` in your views, templated tags, etc.
    Use ``CurrentSiteBaseManager`` to retrieve object on current site.'''
    
    def published(self):
        return super(BaseManager, self).get_query_set().filter( 
                        Q(is_active=True), 
                        Q(pub_date__lte=NOW),
                        Q(pub_end_date__gt=NOW) | Q(pub_end_date__isnull=True),
                    )
    active = published
    
class CurrentSiteBaseManager(BaseManager, CurrentSiteManager):
    pass
    