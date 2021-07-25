from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from django_quill.fields import QuillField
from clubs.models import ClubProfile


class Event(models.Model):
    event_title = models.CharField(max_length=255, unique=True)
    time = models.TimeField(default=None)
    date = models.DateField(default=None)
    event_poster = models.ImageField(upload_to="event_poster/", default="event_poster/eve.jpeg", max_length=1024)
    event_banner = models.ImageField(upload_to="event_banner/", default="event_banner/eve.jpeg", max_length=1024)
    description = QuillField(blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(ClubProfile, default=1, on_delete=models.CASCADE, related_name="user_event_creator")
    participants = models.ManyToManyField(CustomUser, default="none", blank=True, related_name="participants")
    proposal = QuillField(blank=True, default=None, null=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.event_title

    class Meta:
        ordering = ('created', )


class EventStats(models.Model):
    event = models.OneToOneField(Event, default=None, on_delete=models.CASCADE, related_name="eventstats")
    total_participants = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.event.event_title


@receiver(models.signals.post_save, sender=Event)
def post_save_user_signal(sender, instance, created, **kwargs):
    if created:
        instance.save()


def create_event_stats(sender, instance, created, **kwargs):
    if created:
        EventStats.objects.create(event=instance)


post_save.connect(create_event_stats, sender=Event)


class Rating(models.Model):
    event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE, related_name="eventrating")
    user = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE, related_name="rating")
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.event.event_title

