# celery.py
from celery import Celery
from celery.schedules import crontab
from __future__ import absolute_import, unicode_literals
import os

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sl_lmis.settings')

app = Celery('jobs')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Define a periodic task to run the management command every day at midnight (adjust as needed)
app.conf.beat_schedule = {
    'update_job_statuses': {
        'task': 'your_app.tasks.update_job_statuses',  # Change to the correct path
        'schedule': crontab(minute=0, hour=0),
    },
}
