# Generated by Django 3.2.5 on 2021-07-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_rating_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='extra_docs',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
