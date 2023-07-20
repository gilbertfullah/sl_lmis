from django.db import models
from jobs.models import Job
from accounts.models import Company

class EmploymentStatistics(models.Model):
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    date = models.DateField()
    unemployed = models.IntegerField()
    employed = models.IntegerField()
    employment_rate = models.DecimalField(max_digits=5, decimal_places=2)
    unemployment_rate = models.DecimalField(max_digits=5, decimal_places=2)
    job_growth_rate = models.DecimalField(max_digits=5, decimal_places=2)
    average_salary = models.DecimalField(max_digits=10, decimal_places=2)
    industry_trend = models.CharField(max_length=255)
    
class EmployerInsights(models.Model):
    employer = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    employee_turnover_rate = models.DecimalField(max_digits=5, decimal_places=2)
    average_salary = models.DecimalField(max_digits=10, decimal_places=2)
    most_common_job_title = models.CharField(max_length=255)
    most_common_skill = models.CharField(max_length=255)
    job_posting_frequency = models.IntegerField()
    required_experience = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Industry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class SalaryInformation(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    benefits = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job.name} Salary"
    
class IndustrialRelation(models.Model):
    case_number = models.CharField(max_length=50)
    date = models.DateField()
    complainant_name = models.CharField(max_length=100)
    complainant_gender = models.CharField(max_length=10)
    complaint_nature = models.CharField(max_length=200)
    employer_name = models.CharField(max_length=100)
    investigating_officer_name = models.CharField(max_length=100)
    complaint_status = models.CharField(max_length=50)
    settlement_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
class SalaryInformation(models.Model):
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    date = models.DateField()
    median_salary = models.DecimalField(max_digits=10, decimal_places=2)
    average_salary = models.DecimalField(max_digits=10, decimal_places=2)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    
class IndustryTrends(models.Model):
    industry = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    trend = models.CharField(max_length=255)
    growth_rate = models.DecimalField(max_digits=5, decimal_places=2)
    expected_job_openings = models.IntegerField()