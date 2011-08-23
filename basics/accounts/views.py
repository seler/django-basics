from django.views.generic import DetailView
from basics.accounts.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class UserProfileDetail(DetailView):
    model = UserProfile
    queryset = UserProfile.objects.published()
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

class SelfUserProfileDetail(UserProfileDetail):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        queryset = queryset.filter(user__id=self.request.user.id)

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(u'User not logged in')
        return obj
    