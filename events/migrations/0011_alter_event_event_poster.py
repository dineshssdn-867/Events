# Generated by Django 3.2.5 on 2021-07-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_proposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_poster',
            field=models.ImageField(default='event_poster/eve.jpeg', max_length=1024, upload_to='event_poster/'),
        ),
    ]
