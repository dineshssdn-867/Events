from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django_quill.fields import QuillField
from users.models import CustomUser


class ClubProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="profile")
    club_name = models.CharField(max_length=255, default="club")
    logo = models.ImageField(upload_to="club_logo/", default="clubs/static/the-club-1-logo.png", max_length=1024)
    club_banner = models.ImageField(upload_to="club_logo/", default="clubs/static/the-club-1-logo.png", max_length=1024)
    moto = QuillField(blank=False, default=None)
    social_insta = models.URLField(null=True, blank=True)
    social_face = models.URLField(null=True, blank=True)
    social_twitter = models.URLField(null=True, blank=True)
    members = models.ManyToManyField(CustomUser, related_name="members")

    def __str__(self):
        return self.club_name + str(self.id)


@receiver(models.signals.post_save, sender=CustomUser)
def post_save_user_signal(sender, instance, created, **kwargs):
    if created:
        instance.save()


def create_user_profile(sender, instance, created, **kwargs):
    if created and CustomUser.objects.filter(username=instance).values('is_club_member')[0]['is_club_member']:
        ClubProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=CustomUser)

@receiver(models.signals.pre_delete, sender=CustomUser)
def delete_user_profile(sender, instance, **kwargs):
    if CustomUser.objects.filter(username=instance).values('is_club_member')[0]['is_club_member']:
        ClubProfile.objects.filter(user=instance).delete()


pre_delete.connect(delete_user_profile, sender=CustomUser)


