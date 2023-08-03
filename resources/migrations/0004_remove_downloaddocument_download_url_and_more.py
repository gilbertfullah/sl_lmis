# Generated by Django 4.1.1 on 2023-08-03 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_remove_downloaddocument_document_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloaddocument',
            name='download_url',
        ),
        migrations.AddField(
            model_name='downloaddocument',
            name='document',
            field=models.FileField(default=datetime.datetime(2023, 8, 3, 23, 53, 33, 766941, tzinfo=datetime.timezone.utc), upload_to='documents/'),
            preserve_default=False,
        ),
    ]
