from django.db import models
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField


class happy_blog(models.Model):
    name = models.CharField(_('Name'),max_length=200)
    job_type = models.CharField(_('Job Type'), max_length=300)
    tweet = QuillField(_('tweet'), blank=True)
    image = models.ImageField(_('image'), upload_to="happy_blog/", default="media/happy_blog/images.png", max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
