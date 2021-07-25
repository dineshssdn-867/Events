from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import CreateView
from happy_blog.forms import HappyBlogForm
from happy_blog.models import happy_blog
from functools import lru_cache


@method_decorator(login_required(login_url='/user/login'), name='dispatch')
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class HappyBlogView(CreateView):
    template_name = 'happy_blog/happy-blog.html'
    model = happy_blog
    form_class = HappyBlogForm
    success_url = '/'

    def form_valid(self, form: Any) -> Dict[str, Any]:
        instance = form.save(commit=False)
        instance.save(using='blogs')
        return super(HappyBlogView, self).form_valid(form)
