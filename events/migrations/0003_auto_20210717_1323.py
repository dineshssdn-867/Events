# Generated by Django 3.2.5 on 2021-07-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('created',)},
        ),
        migrations.AlterField(
            model_name='event',
            name='event_banner',
            field=models.ImageField(default='event_banner/eve.jpeg', upload_to='event_banner/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_poster',
            field=models.ImageField(default='event_poster/eve.jpeg', upload_to='event_poster/'),
        ),
    ]
