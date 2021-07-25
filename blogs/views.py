from functools import lru_cache

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import *


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="default"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class HomeView(ListView):
    template_name = 'blogs/blogs.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="default"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class CreateBlogView(SuccessMessageMixin, CreateView):
    model = Blog
    template_name = 'blogs/blog-add.html'
    success_url = '/'
    success_message = "Event has been posted"
    form_class = CreateBlog

    def form_valid(self, form):
        form = CreateBlog(self.request.POST, self.request.FILES)
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        return super(CreateBlogView, self).form_valid(form)

@method_decorator(lru_cache(maxsize=None), name='dispatch')
class SingleBlogView(UpdateView, SuccessMessageMixin):
    template_name = 'blogs/blog-single.html'
    model = Blog
    context_object_name = 'blog'
    form_class = LikeForm
    success_message = "You applied for this job"

    def get_context_data(self, **kwargs):
        context = super(SingleBlogView, self).get_context_data(**kwargs)
        context['blogss'] = Blog.objects.all()
        context['blogs'] = Blog.objects.filter(id=self.object.pk)
        for stats in context['blogs']:
            clicks = stats.clicks
        clicks = clicks + 1
        Blog.objects.filter(id=self.object.pk).update(clicks=clicks)
        context['Liked'] = Blog.objects.get(pk=self.object.pk).likes.all().filter(id=self.request.user.id)
        context['likes'] = context['blog'].total_likes()
        return context

    def form_valid(self, form):
        participant = self.request.user
        form.instance.likes.add(participant)
        form.save()
        return super(SingleBlogView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blogs:single_blog', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="default"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class UpdateBlogView(SuccessMessageMixin, UpdateView):
    model = Blog
    template_name = 'blogs/blog-update.html'
    form_class = UpdateBlogForm
    success_message = "You updated your blog!"
    success_url = '/'

    def form_valid(self, form):
        form = UpdateBlogForm(self.request.POST, self.request.FILES, instance=Blog.objects.get(pk=self.object.pk))
        form.instance.user = self.request.user
        return super(UpdateBlogView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UpdateBlogView, self).get(request, *args, **kwargs)


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="default"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class DeleteBlogView(SuccessMessageMixin, DeleteView):
    model = Blog
    success_url = '/'
    template_name = 'blogs/blog-delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')

        return super(DeleteBlogView, self).get(request, *args, **kwargs)
