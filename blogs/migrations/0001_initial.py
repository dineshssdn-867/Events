# Generated by Django 3.2.5 on 2021-07-17 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255, unique=True)),
                ('blog_poster', models.ImageField(default='event_poster/eve.jpeg', upload_to='event_poster/')),
                ('blog_banner', models.ImageField(default='event_banner/eve.jpeg', upload_to='event_banner/')),
                ('description', django_quill.fields.QuillField(default=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('clicks', models.IntegerField(default=0)),
                ('likes', models.ManyToManyField(blank=True, default='none', related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_blog', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
