from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from django_quill.fields import QuillField


class Blog(models.Model):
    blog_title = models.CharField(max_length=255, unique=True)
    blog_poster = models.ImageField(upload_to="event_poster/", default="event_poster/eve.jpeg", max_length=1024)
    blog_banner = models.ImageField(upload_to="event_banner/", default="event_banner/eve.jpeg", max_length=1024)
    description = QuillField(blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE, related_name="user_blog")
    likes = models.ManyToManyField(CustomUser, default="none", blank=True, related_name="likes")
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.blog_title

    class Meta:
        ordering = ('created', )

    def total_likes(self):
        return self.likes.all().count()


