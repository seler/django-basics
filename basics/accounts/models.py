from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')

    # Other fields here
    accepted_eula = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default="Dragons.")
    
    def __unicode__(self):
        return _("%s's profile") % self.user.__unicode__()

    def test(self):
        return _("%s's profile") % self.user.__unicode__()
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
