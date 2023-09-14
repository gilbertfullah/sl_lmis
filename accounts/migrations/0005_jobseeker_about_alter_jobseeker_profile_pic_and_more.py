# Generated by Django 4.1.1 on 2023-09-13 11:32

import accounts.models
import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_employer_district_alter_government_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='about',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='profile_pic',
            field=models.FileField(upload_to=accounts.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg']), accounts.models.validate_image_type]),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(default=django.utils.timezone.now, upload_to='resumes/', validators=[django.core.validators.FileExtensionValidator(['pdf']), accounts.models.validate_file_mimetype]),
            preserve_default=False,
        ),
    ]
