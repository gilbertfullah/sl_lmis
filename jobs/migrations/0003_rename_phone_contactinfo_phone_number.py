# Generated by Django 4.1.1 on 2023-09-13 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_contactinfo_resume_application'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
