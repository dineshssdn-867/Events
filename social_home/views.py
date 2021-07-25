from functools import lru_cache

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import ListView
from blogs.models import Blog
from clubs.models import ClubProfile
from events.models import Event
from happy_blog.models import happy_blog


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="default"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class HomeView(ListView):
    template_name = 'main/index.html'
    model = happy_blog
    context_object_name = 'happy_blogs'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['happy_blog'] = happy_blog.objects.using('blogs').all()
        context['blogs'] = Blog.objects.all()
        context['clubprofiles'] = ClubProfile.objects.all()
        context['clubprofile'] = len(context['clubprofiles'])
        context['events'] = Event.objects.all().count()
        return context

