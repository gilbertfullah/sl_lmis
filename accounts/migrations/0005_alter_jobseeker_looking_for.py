# Generated by Django 4.1.1 on 2023-01-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='looking_for',
            field=models.CharField(max_length=30),
        ),
    ]
