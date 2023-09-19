# Generated by Django 4.1.1 on 2023-09-19 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmploymentStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('unemployed', models.IntegerField()),
                ('employed', models.IntegerField()),
                ('employment_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unemployment_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('job_growth_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('industry_trend', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IndustrialRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('complainant_name', models.CharField(max_length=100)),
                ('complainant_gender', models.CharField(max_length=10)),
                ('complaint_nature', models.CharField(max_length=200)),
                ('employer_name', models.CharField(max_length=100)),
                ('investigating_officer_name', models.CharField(max_length=100)),
                ('complaint_status', models.CharField(max_length=50)),
                ('settlement_fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryTrends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('trend', models.CharField(max_length=255)),
                ('growth_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expected_job_openings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SalaryInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('median_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='EmployerInsights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee_turnover_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('most_common_job_title', models.CharField(max_length=255)),
                ('most_common_skill', models.CharField(max_length=255)),
                ('job_posting_frequency', models.IntegerField()),
                ('required_experience', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employer')),
            ],
        ),
    ]
