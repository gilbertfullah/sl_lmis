# Generated by Django 4.1.1 on 2023-07-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]