from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from basics.accounts.managers import UserProfileManager

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    is_active = models.BooleanField(verbose_name=_('active'), default=False, help_text=_("Tick to make this entry live (see also the publication date). Note that administrators (like yourself) are allowed to preview inactive entries whereas the general public aren't."))
    creation_date = models.DateTimeField(verbose_name=_('creation date'), auto_now_add=True, editable=False, null=True, blank=True)
    last_mod_date = models.DateTimeField(auto_now=True, verbose_name=_("last modification date"), null=True, blank=True)
    
    is_email_public = models.BooleanField(verbose_name=_('is email public'), default=False)
    
    objects = UserProfileManager()
    
    def __unicode__(self):
        return _("%s's profile") % self.user.__unicode__()

    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
