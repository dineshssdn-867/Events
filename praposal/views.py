from functools import lru_cache

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mass_mail
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import UpdateView, DeleteView, ListView
from blogs.models import *
from clubs.models import ClubProfile
from events.models import EventStats
from .forms import *


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache2"), name='dispatch')
class ProposalView(ListView):
    template_name = 'proposals/proposals.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProposalView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(is_accepted=False)
        return context


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache2"), name='dispatch')
class ProposalClubView(ListView):
    template_name = 'proposals/proposals-club.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProposalClubView, self).get_context_data(**kwargs)
        profile = ClubProfile.objects.filter(user=self.request.user)
        context['events'] = Event.objects.filter(is_accepted=False).filter(user=profile[0])
        return context


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache2"), name='dispatch')
class SingleProposalView(UpdateView, SuccessMessageMixin):
    template_name = 'proposals/proposals-single.html'
    model = Event
    context_object_name = 'event'
    success_url = '/'
    form_class = AcceptEventForm
    success_message = "You accepted this event"

    def get_context_data(self, **kwargs):
        context = super(SingleProposalView, self).get_context_data(**kwargs)
        context['blogss'] = Blog.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.is_accepted = True
        form.save()
        receivers = [self.object.user.user.email]
        datatuple = (
            ('Event Accepted '+str(self.object.event_title), "Your event has been accepted. Congratulations", 'dinesh.n@ahduni.edu.in', receivers),
        )
        send_mass_mail(datatuple)
        receivers = []
        recipients = ClubProfile.objects.get(pk=self.object.pk).members.all().values('email')
        print(recipients)
        for recipient in recipients:
             receivers.append(recipient['email'])
        message = '''
            Event Details:-
            Event Title: ''' + str(self.object.event_title) +  '''
            Event Date: ''' + str(self.object.date) + '''
            Event Time: ''' + str(self.object.time)
        datatuple = (
             ('Event announcement '+ str(self.object.event_title), message, 'dinesh.n@ahduni.edu.in', receivers),
        )
        send_mass_mail(datatuple)
        return super(SingleProposalView, self).form_valid(form)


@method_decorator(login_required(login_url='/user/login'), name="dispatch")
@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="cache2"), name='dispatch')
class DeleteProposalView(SuccessMessageMixin, DeleteView):

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user or request.user.is_superuser:
            self.object.delete()
            receivers = [self.object.user.user.email]
            datatuple = (
                ('Event Rejected ' + str(self.object.event_title), "Your event has been rejected. Sorry but please try to apply for a better event next time. \
                                                                 For any querys please send a mail from contact us page we will reply.",
                 'dinesh.n@ahduni.edu.in', receivers),
            )
            send_mass_mail(datatuple)
            EventStats.objects.filter(event=self.object.pk).delete()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.user.is_superuser)
        if self.object.user != request.user and not request.user.is_superuser:
            return HttpResponseRedirect('/')

        return super(DeleteProposalView, self).get(request, *args, **kwargs)
