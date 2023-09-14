# your_app/tasks.py
from celery import shared_task
from django.core.management import call_command

@shared_task
def update_job_statuses():
    call_command('update_job_statuses')
