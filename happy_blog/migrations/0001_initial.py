# Generated by Django 3.2.5 on 2021-07-17 07:53

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='happy_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('job_type', models.CharField(max_length=300, verbose_name='Job Type')),
                ('tweet', django_quill.fields.QuillField(blank=True, max_length=300, verbose_name='Resume')),
                ('image', models.ImageField(default='media/happy_blog/images.png', upload_to='media/happy_blog', verbose_name='image')),
            ],
        ),
    ]
