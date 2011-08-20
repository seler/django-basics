from django.views.generic import DetailView
from basics.categories.models import Category
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse
from django.core.xheaders import populate_xheaders
from django.views.decorators.csrf import csrf_protect


class CategoryDetailView(DetailView):
    queryset = Category.objects.published()
    def get_object(self):
        objects = Category.objects.published()
        try:
            return (object for object in objects if object.path.lstrip('/').rstrip('/') == self.kwargs['path']).next()
        except StopIteration:
            raise Http404
        

def category(request, path):
    objects = Category.objects.published()
    try:
        category =  (object for object in objects if object.get_absolute_url().lstrip('/').rstrip('/') == path.lstrip('/').rstrip('/')).next()
    except StopIteration:
        raise Http404

    return render_category(request, category)

@csrf_protect
def render_category(request, category):
    t = loader.get_template('categories/category_detail.html')
    c = RequestContext(request, {
        'category': category,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, Category, category.id)
    return response
