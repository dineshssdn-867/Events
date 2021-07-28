import datetime
from datetime import date
from functools import lru_cache

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F,Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from blogs.models import *
from .forms import *


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class UpcomingEventView(ListView):
    template_name = 'events/events-upcoming.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UpcomingEventView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(date__gt=date.today()).filter(is_accepted=True)
        return context


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class PastEventView(ListView):
    template_name = 'events/events-past.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PastEventView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(date__lt=date.today()).filter(is_accepted=True)
        return context


@method_decorator(login_required(login_url='/users/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class ClubsEventView(ListView):
    template_name = 'events/events-club.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ClubsEventView, self).get_context_data(**kwargs)
        profile = ClubProfile.objects.get(user=self.request.user)
        context['events'] = Event.objects.filter(user=profile).filter(is_accepted=True)
        return context


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class TodayEventView(ListView):
    template_name = 'events/events-today.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TodayEventView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(date=date.today()).filter(is_accepted=True)
        return context


@method_decorator(login_required(login_url='/users/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class CreateEventView(SuccessMessageMixin, CreateView):
    model = Event
    template_name = 'events/events-add.html'
    success_url = '/'
    success_message = "Event has been posted"
    form_class = CreateEvent

    def form_valid(self, form):
        form = CreateEvent(self.request.POST, self.request.FILES)
        event = form.save(commit=False)
        event.user = ClubProfile.objects.filter(user=self.request.user)[0]
        event.save()
        return super(CreateEventView, self).form_valid(form)


class SingleEventView(UpdateView, SuccessMessageMixin):
    template_name = 'events/events-single.html'
    model = Event
    context_object_name = 'event'
    form_class = ApplyEventForm
    success_message = "You applied for this event"

    def get_context_data(self, **kwargs):
        context = super(SingleEventView, self).get_context_data(**kwargs)
        context['event_stats'] = EventStats.objects.filter(event=self.object.pk)
        current_time = datetime.datetime.now() - datetime.timedelta(days=1)
        if datetime.datetime(self.object.date.year, self.object.date.month, self.object.date.day) < current_time:
            context['allow'] = True
        else:
            context['allow'] = False
        context['blogss'] = Blog.objects.all()
        EventStats.objects.filter(event=self.object.pk).update(clicks=F('clicks')+1)
        context['registered'] = Event.objects.get(pk=self.object.pk).participants.all().filter(id=self.request.user.id)
        if self.request.user.is_authenticated:
            context['not_rated']=True
            if Rating.objects.filter(Q(event=self.object.pk) & Q(user=self.request.user)):
                context['not_rated'] = False
        return context

    def form_valid(self, form):
        participant = self.request.user
        form.instance.participants.add(participant)
        form.save()
        participants = Event.objects.get(pk=self.object.pk).participants.all().count()
        EventStats.objects.filter(event=self.object.pk).update(total_participants=participants)
        return super(SingleEventView, self).form_valid(form)

    def get_success_url(self):
        return reverse('events:single_event', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch')
class UpdateEventView(SuccessMessageMixin, UpdateView, ListView):
    model = Event
    template_name = 'events/events-update.html'
    form_class = UpdateEventForm
    success_message = "You updated your event!"

    def form_valid(self, form):
        form = UpdateEventForm(self.request.POST, self.request.FILES, instance=Event.objects.get(pk=self.object.pk))
        form.instance.user = ClubProfile.objects.filter(user=self.request.user)[0]
        return super(UpdateEventView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdateEventView, self).get_context_data()
        if self.object.time.hour < 10:
            context['hour'] = '0' + str(self.object.time.hour)
        else:
            context['hour'] = str(self.object.time.hour)

        if self.object.time.minute < 10:
            context['minutes'] = '0' + str(self.object.time.minute)
        else:
            context['minutes'] = str(self.object.time.minute)

        if self.object.date.month < 10:
            context['month'] = '0' + str(self.object.date.month)
        else:
            context['month'] = str(self.object.date.month)

        if self.object.date.day < 10:
            context['day'] = '0' + str(self.object.date.day)
        else:
            context['day'] = str(self.object.date.day)
        context['year'] = self.object.date.year
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user.user != request.user:
            return HttpResponseRedirect('/')
        return super(UpdateEventView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('events:update_event', kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
class DeleteEventView(SuccessMessageMixin, DeleteView):
    model = Event
    success_url = '/'
    template_name = 'events/events-delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user.user != request.user:
            return HttpResponseRedirect('/')

        return super(DeleteEventView, self).get(request, *args, **kwargs)


@login_required(login_url='/user/login')
@vary_on_headers('User-Agent', 'Cookie')
@cache_page(60 * .167, cache="cache1")
def CreateRatingView(request, *args, **kwargs):
    rating = Rating()
    rating.event = Event.objects.get(pk=kwargs['pk'])
    rating.user = request.user
    registered =  Event.objects.get(pk=kwargs['pk']).participants.all().filter(id=request.user.id)
    current_time = datetime.datetime.now() - datetime.timedelta(days=1)
    if datetime.datetime(rating.event.date.year, rating.event.date.month, rating.event.date.day) < current_time and registered:
        rating.rating = request.POST.get('rating')
        rating.save()
        EventStats.objects.filter(event=kwargs['pk']).update(
        rating=(F('rating') + rating.rating) / 2)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache1"), name='dispatch')
class CalenderEventView(ListView):
    template_name = 'events/events-calender.html'
    model = Event
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super(CalenderEventView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context
