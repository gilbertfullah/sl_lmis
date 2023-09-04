# Generated by Django 4.1.1 on 2023-09-04 22:51

import accounts.models
import ckeditor.fields
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
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('profile_pic', models.ImageField(upload_to=accounts.models.user_directory_path)),
                ('district', models.CharField(choices=[('', 'Select a district'), ('Bo', 'Bo'), ('Bonthe', 'Bonthe'), ('Bombali', 'Bombali'), ('Falaba', 'Falaba'), ('Kailahun', 'Kailahun'), ('Kambia', 'Kambia'), ('Kenema', 'Kenema'), ('Koinadugu', 'Koinadugu'), ('Karene', 'Karene'), ('Kono', 'Kono'), ('Moyamba', 'Moyamba'), ('Port Loko', 'Port Loko'), ('Pujehun', 'Pujehun'), ('Tonkolili', 'Tonkolili'), ('Western Rural', 'Western Rural'), ('Western Urban', 'Western Urban')], max_length=250)),
                ('education_level', models.CharField(max_length=200)),
                ('profession', models.CharField(blank=True, max_length=200, null=True)),
                ('qualification', models.CharField(max_length=250)),
                ('grad_year', models.CharField(max_length=4)),
                ('resume', models.FileField(blank=True, null=True, upload_to='')),
                ('looking_for', models.CharField(max_length=30)),
                ('employment_status', models.CharField(choices=[('', 'Select employment staus'), ('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed'), ('Student', 'Student'), ('Retired', 'Retired')], max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'JobSeekers',
            },
        ),
        migrations.CreateModel(
            name='JobSeekerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=250, verbose_name='School/College/University')),
                ('grad_year', models.CharField(blank=True, max_length=4, null=True)),
                ('degree', models.CharField(blank=True, max_length=200, null=True)),
                ('field_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250)),
                ('employer', models.CharField(max_length=250)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('job_description', ckeditor.fields.RichTextField()),
                ('cv', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('about', ckeditor.fields.RichTextField()),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('pic', models.ImageField(upload_to=accounts.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('district', models.CharField(choices=[('', 'Select a district'), ('Bo', 'Bo'), ('Bonthe', 'Bonthe'), ('Bombali', 'Bombali'), ('Falaba', 'Falaba'), ('Kailahun', 'Kailahun'), ('Kambia', 'Kambia'), ('Kenema', 'Kenema'), ('Koinadugu', 'Koinadugu'), ('Karene', 'Karene'), ('Kono', 'Kono'), ('Moyamba', 'Moyamba'), ('Port Loko', 'Port Loko'), ('Pujehun', 'Pujehun'), ('Tonkolili', 'Tonkolili'), ('Western Rural', 'Western Rural'), ('Western Urban', 'Western Urban')], max_length=250)),
                ('phone_number', models.CharField(max_length=50)),
                ('sector', models.CharField(choices=[('', 'Select a category'), ('Agriculture, Fishing, Aquaculture', 'Agriculture, Fishing, Aquaculture'), ('Trade and Investment', 'Trade and Investment'), ('Wholesale and retail trade', 'Wholesale and retail trade'), ('Mining, Chemistry, Petrochemistry, raw materials', 'Mining, Chemistry, Petrochemistry, raw materials'), ('Government Services', 'Government Services'), ('Manufacturing and handicrafts', 'Manufacturing and handicrafts'), ('Construction', 'Construction'), ('Electricity and water', 'Electricity and water'), ('Telecommunications', 'Telecommunications'), ('Transport and Logistics', 'Transport and Logistics'), ('Tourism, Hotel business and Catering', 'Tourism, Hotel business and Catering'), ('Audit, Advice, Accounting', 'Audit, Advice, Accounting'), ('Health, Social Professions', 'Health, Social Professions'), ('HR', 'HR'), ('IT, Software engineering, Internet', 'IT, Software engineering, Internet'), ('Legal', 'Legal'), ('Management', 'Management'), ('Marketing, Communication, Media', 'Marketing, Communication, Media'), ('R&D, Project Management', 'R&D, Project Management'), ('Sales', 'Sales'), ('Services', 'Services'), ('Public buildings and Works profession', 'Public buildings and Works profession'), ('Purchases', 'Purchases'), ('Airport and Shipping Services', 'Airport and Shipping Services'), ('Banking, Insurance, Finance', 'Airport and Shipping Services'), ('Associative activities', 'Associative activities'), ('Call centers, Hotlines', 'Call centers, Hotlines'), ('Cleaning, Security, Surveillance', 'Cleaning, Security, Surveillance'), ('Edition, Printing', 'Edition, Printing'), ('Education, Training', 'Education, Training'), ('Electric, Electronics, Optical and Precision equipments', 'Electric, Electronics, Optical and Precision equipments'), ('Engineering, Development studies', 'Engineering, Development studies'), ('Environment, Recycling', 'Environment, Recycling'), ('Event, Receptionist', 'Event, Receptionist'), ('Food processing', 'Food processing'), ('Health, Pharmacy, Hospital, Medical equipments', 'Health, Pharmacy, Hospital, Medical equipments'), ('Import, Export', 'Import, Export'), ('Cosmetics', 'Cosmetics'), ('Sports, Cultural and Social action', 'Sports, Cultural and Social action'), ('Others', 'Others')], max_length=250)),
                ('logo', models.ImageField(upload_to=accounts.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Government',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=50)),
                ('district', models.CharField(choices=[('', 'Select a district'), ('Bo', 'Bo'), ('Bonthe', 'Bonthe'), ('Bombali', 'Bombali'), ('Falaba', 'Falaba'), ('Kailahun', 'Kailahun'), ('Kambia', 'Kambia'), ('Kenema', 'Kenema'), ('Koinadugu', 'Koinadugu'), ('Karene', 'Karene'), ('Kono', 'Kono'), ('Moyamba', 'Moyamba'), ('Port Loko', 'Port Loko'), ('Pujehun', 'Pujehun'), ('Tonkolili', 'Tonkolili'), ('Western Rural', 'Western Rural'), ('Western Urban', 'Western Urban')], max_length=250)),
                ('company_logo', models.ImageField(upload_to=accounts.models.user_directory_path)),
                ('company_certificate', models.FileField(upload_to='')),
                ('company_size', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('sector', models.CharField(choices=[('', 'Select a category'), ('Agriculture, Fishing, Aquaculture', 'Agriculture, Fishing, Aquaculture'), ('Trade and Investment', 'Trade and Investment'), ('Wholesale and retail trade', 'Wholesale and retail trade'), ('Mining, Chemistry, Petrochemistry, raw materials', 'Mining, Chemistry, Petrochemistry, raw materials'), ('Government Services', 'Government Services'), ('Manufacturing and handicrafts', 'Manufacturing and handicrafts'), ('Construction', 'Construction'), ('Electricity and water', 'Electricity and water'), ('Telecommunications', 'Telecommunications'), ('Transport and Logistics', 'Transport and Logistics'), ('Tourism, Hotel business and Catering', 'Tourism, Hotel business and Catering'), ('Audit, Advice, Accounting', 'Audit, Advice, Accounting'), ('Health, Social Professions', 'Health, Social Professions'), ('HR', 'HR'), ('IT, Software engineering, Internet', 'IT, Software engineering, Internet'), ('Legal', 'Legal'), ('Management', 'Management'), ('Marketing, Communication, Media', 'Marketing, Communication, Media'), ('R&D, Project Management', 'R&D, Project Management'), ('Sales', 'Sales'), ('Services', 'Services'), ('Public buildings and Works profession', 'Public buildings and Works profession'), ('Purchases', 'Purchases'), ('Airport and Shipping Services', 'Airport and Shipping Services'), ('Banking, Insurance, Finance', 'Airport and Shipping Services'), ('Associative activities', 'Associative activities'), ('Call centers, Hotlines', 'Call centers, Hotlines'), ('Cleaning, Security, Surveillance', 'Cleaning, Security, Surveillance'), ('Edition, Printing', 'Edition, Printing'), ('Education, Training', 'Education, Training'), ('Electric, Electronics, Optical and Precision equipments', 'Electric, Electronics, Optical and Precision equipments'), ('Engineering, Development studies', 'Engineering, Development studies'), ('Environment, Recycling', 'Environment, Recycling'), ('Event, Receptionist', 'Event, Receptionist'), ('Food processing', 'Food processing'), ('Health, Pharmacy, Hospital, Medical equipments', 'Health, Pharmacy, Hospital, Medical equipments'), ('Import, Export', 'Import, Export'), ('Cosmetics', 'Cosmetics'), ('Sports, Cultural and Social action', 'Sports, Cultural and Social action'), ('Others', 'Others')], max_length=250)),
                ('status', models.CharField(choices=[('', 'Select a status'), ('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Employers',
            },
        ),
        migrations.CreateModel(
            name='ProfileView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.jobseeker')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('viewer', 'jobseeker')},
            },
        ),
    ]
