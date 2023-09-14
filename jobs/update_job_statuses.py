# your_app/management/commands/update_job_statuses.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from .models import Job  # Import your Job model

class Command(BaseCommand):
    help = 'Update job statuses and set is_active flag based on expiration date'

    def handle(self, *args, **kwargs):
        # Get all jobs with expiration date in the past and status "Approved"
        expired_jobs = Job.objects.filter(
            expiration_date__lt=timezone.now(),
            job_status='Approved'
        )

        for job in expired_jobs:
            job.job_status = 'Closed'
            job.is_active = False
            job.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated job statuses'))
