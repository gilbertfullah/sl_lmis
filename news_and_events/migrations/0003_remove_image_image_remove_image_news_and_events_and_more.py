# Generated by Django 4.1.1 on 2023-07-24 16:40

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_and_events', '0002_remove_newsandevents_images_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='news_and_events',
        ),
        migrations.AddField(
            model_name='image',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(default='images/home-blog1.jpg', upload_to='news/'), default=datetime.datetime(2023, 7, 24, 16, 40, 27, 452263, tzinfo=datetime.timezone.utc), size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsandevents',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='newsandevents',
            name='images',
            field=models.ForeignKey(default=datetime.datetime(2023, 7, 24, 16, 40, 37, 300285, tzinfo=datetime.timezone.utc), on_delete=django.db.models.deletion.CASCADE, related_name='news_and_events', to='news_and_events.image'),
            preserve_default=False,
        ),
    ]
