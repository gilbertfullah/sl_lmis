# Generated by Django 4.1.1 on 2023-08-03 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_remove_downloaddocument_download_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloaddocument',
            name='document',
        ),
        migrations.AddField(
            model_name='downloaddocument',
            name='download_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]