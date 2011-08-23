from django.db import models

class UserProfileManager(models.Manager):
    def published(self):
        return super(UserProfileManager, self).get_query_set().filter(is_active=True)
    active = published
