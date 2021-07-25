from functools import lru_cache

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import ListView
from happy_blog.models import *


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
class AboutusView(ListView):
    template_name = 'aboutus/aboutus.html'
    model = happy_blog
    context_object_name = 'happy_blogs'

    @lru_cache(maxsize=None)
    def get_context_data(self, **kwargs):
        context = super(AboutusView, self).get_context_data(**kwargs)
        context['happy_blog'] = happy_blog.objects.using('blogs').all() 
        print(context)
        return context

