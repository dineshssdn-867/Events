# Generated by Django 3.2.5 on 2021-07-21 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20210721_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubprofile',
            old_name='member',
            new_name='members',
        ),
    ]
