from functools import lru_cache

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import UpdateView, ListView
from .forms import *
from events.models import Event


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache2"), name='dispatch')
class ClubsView(ListView):
    template_name = 'clubs/clubs.html'
    model = ClubProfile
    context_object_name = 'clubs'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ClubsView, self).get_context_data(**kwargs)
        context['clubs'] = ClubProfile.objects.filter(user__is_allowed=True)
        return context

@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * 1, cache="cache2"), name='dispatch')
class SingleClubView(UpdateView, SuccessMessageMixin):
    template_name = 'clubs/club-single.html'
    model = ClubProfile
    context_object_name = 'club'
    form_class = ApplyMemberForm
    success_message = "You are member of this club"

    @lru_cache(maxsize=None)
    def get_context_data(self, **kwargs):
        context = super(SingleClubView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(user=self.object.pk)
        context['registered'] = ClubProfile.objects.get(pk=self.object.pk).members.all().filter(id=self.request.user.id)
        return context

    def form_valid(self, form):
        member = self.request.user
        form.instance.members.add(member)
        form.save()
        return super(SingleClubView, self).form_valid(form)

    def get_success_url(self):
        return reverse('clubs:single_club', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/users/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * 1, cache="cache2"), name='dispatch')
class UpdateClubView(SuccessMessageMixin, UpdateView):
    model = ClubProfile
    template_name = 'clubs/club-update.html'
    form_class = UpdateClubForm
    success_message = "You updated your club!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateClubView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UpdateClubView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('clubs:update_club', kwargs={"pk": self.object.pk})
