# Generated by Django 3.2.5 on 2021-07-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_extra_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='extra_docs',
            field=models.FileField(blank=True, default=None, null=True, upload_to='event_docs/'),
        ),
    ]
