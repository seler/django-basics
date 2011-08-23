from django.views.generic import DetailView
from basics.pages.models import Page

class PageDetailView(DetailView):
    model = Page
    def get(self, request, **kwargs):
        self.queryset = Page.objects.all() if request.user.has_perm('pages.add_page') or request.user.has_perm('pages.change_page') or request.user.has_perm('pages.delete_page') else Page.objects.published()
        self.object = self.get_object()
        if self.object.registration_required and not request.user.is_authenticated():
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(self.request.path)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
