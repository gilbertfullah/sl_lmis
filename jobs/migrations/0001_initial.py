# Generated by Django 4.1.1 on 2022-12-07 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Job Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Job Description')),
                ('location', models.CharField(default='Western Area', max_length=200, verbose_name='Location')),
                ('contract', models.CharField(choices=[('', 'Select a contract type'), ('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Internship', 'Internship'), ('Freelance', 'Freelance')], max_length=100, verbose_name='Contract-Type')),
                ('sector', models.CharField(default='Accounting', max_length=200, verbose_name='Sector')),
                ('salary', models.CharField(blank=True, max_length=200, null=True, verbose_name='Salary')),
                ('expiration_date', models.DateField()),
                ('experience', models.CharField(choices=[('', 'Select an experience level'), ('No experience', 'No experience'), ('Less than 1 year', 'Less than 1 year'), ('1 - 2 years', '1 - 2 years'), ('2 - 5 years', '2 - 5 years'), ('5 - 10 years', '5 - 10 years'), ('More than 10 years', 'More than 10 years')], max_length=200, verbose_name='Working Experience')),
                ('qualification', models.CharField(default='Bachelors', max_length=200, verbose_name='Qualification')),
                ('requirements', models.TextField(verbose_name='Requirement')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('updated', models.DateField(auto_now=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company')),
                ('favourite', models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Selected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_applicant', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_job', to='jobs.job')),
            ],
        ),
        migrations.CreateModel(
            name='SavedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_job', to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppliedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_job', to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='jobs.job')),
            ],
        ),
    ]
