# Generated by Django 4.1.1 on 2023-07-24 23:00

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_jobseeker', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
                ('is_government', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=200)),
                ('location', models.CharField(choices=[('', 'Select a district'), ('Bo', 'Bo'), ('Bonthe', 'Bonthe'), ('Bombali', 'Bombali'), ('Falaba', 'Falaba'), ('Kailahun', 'Kailahun'), ('Kambia', 'Kambia'), ('Kenema', 'Kenema'), ('Koinadugu', 'Koinadugu'), ('Karene', 'Karene'), ('Kono', 'Kono'), ('Moyamba', 'Moyamba'), ('Port Loko', 'Port Loko'), ('Pujehun', 'Pujehun'), ('Tonkolili', 'Tonkolili'), ('Western Rural', 'Western Rural'), ('Western Urban', 'Western Urban')], max_length=250)),
                ('company_logo', models.FileField(blank=True, null=True, upload_to='')),
                ('company_certificate', models.FileField(upload_to='')),
                ('company_size', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('government_institution_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.CharField(choices=[('', 'Select a district'), ('Bo', 'Bo'), ('Bonthe', 'Bonthe'), ('Bombali', 'Bombali'), ('Falaba', 'Falaba'), ('Kailahun', 'Kailahun'), ('Kambia', 'Kambia'), ('Kenema', 'Kenema'), ('Koinadugu', 'Koinadugu'), ('Karene', 'Karene'), ('Kono', 'Kono'), ('Moyamba', 'Moyamba'), ('Port Loko', 'Port Loko'), ('Pujehun', 'Pujehun'), ('Tonkolili', 'Tonkolili'), ('Western Rural', 'Western Rural'), ('Western Urban', 'Western Urban')], max_length=250)),
                ('phone_number', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=100)),
                ('logo', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='')),
                ('location', models.CharField(choices=[('', 'Select a district'), ('Bo', 'Bo'), ('Bonthe', 'Bonthe'), ('Bombali', 'Bombali'), ('Falaba', 'Falaba'), ('Kailahun', 'Kailahun'), ('Kambia', 'Kambia'), ('Kenema', 'Kenema'), ('Koinadugu', 'Koinadugu'), ('Karene', 'Karene'), ('Kono', 'Kono'), ('Moyamba', 'Moyamba'), ('Port Loko', 'Port Loko'), ('Pujehun', 'Pujehun'), ('Tonkolili', 'Tonkolili'), ('Western Rural', 'Western Rural'), ('Western Urban', 'Western Urban')], max_length=250)),
                ('education_level', models.CharField(max_length=200)),
                ('course_training', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('grad_year', models.CharField(max_length=4)),
                ('resume', models.FileField(blank=True, null=True, upload_to='')),
                ('looking_for', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
