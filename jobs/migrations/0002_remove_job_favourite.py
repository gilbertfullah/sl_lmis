# Generated by Django 4.1.1 on 2022-12-07 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='favourite',
        ),
    ]
