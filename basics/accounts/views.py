from django.views.generic import DetailView
from basics.accounts.models import UserProfile
from django.contrib.auth.models import SiteProfileNotAvailable
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

class UserProfile(TemplateView):
    template_name = "accounts/user_profile.html"
    
class UserProfileDetail(DetailView):
    model = UserProfile
    def get(self, request, **kwargs):
        if not request.user.is_authenticated():
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(self.request.path)
        
        try:
            self.object = request.user.get_profile()
        except SiteProfileNotAvailable:
            #the current site doesn't allow profiles
            pass
#        except ObjectDoesNotExist:
            #the user does not have a profile
#            pass
        
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
