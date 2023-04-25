# Generated by Django 4.1.1 on 2023-01-10 11:52

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_jobseeker_grad_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='course_training',
            field=models.CharField(default=datetime.datetime(2023, 1, 10, 11, 51, 51, 996800, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='profession',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
