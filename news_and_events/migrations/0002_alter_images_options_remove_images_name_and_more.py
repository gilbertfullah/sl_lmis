# Generated by Django 4.1.1 on 2023-07-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_and_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={},
        ),
        migrations.RemoveField(
            model_name='images',
            name='name',
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to=''),
        ),
    ]
