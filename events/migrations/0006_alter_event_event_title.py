# Generated by Django 3.2.5 on 2021-07-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_proposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
