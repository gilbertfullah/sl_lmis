from django_unicorn.components import UnicornView
from jobs.models import Job


class JobFilterView(UnicornView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jobs = jobs = Job.objects.all()
        self.filtered_jobs = None
        self.filters = {'title': None, 'location': None, 'sector': None, 'contract': None}
    
    def filter_jobs(self):
        self.filtered_jobs = []
        for job in self.jobs:
            if (self.filters['title'] is None or job['title'] == self.filters['title']) and \
                    (self.filters['location'] is None or job['location'] == self.filters['location']) and \
                        (self.filters['sector'] is None or job['sector'] == self.filters['sector']) and \
                            (self.filters['contract'] is None or job['contract'] == self.filters['contract']):
                self.filtered_jobs.append(job)

    def reset_filters(self):
        self.filters = {'title': None, 'location': None, 'sector': None, 'contract': None}
        self.filtered_jobs = None

    def render(self):
        if self.filtered_jobs is None:
            jobs = self.jobs
        else:
            jobs = self.filtered_jobs
            
        paginator = Paginator(jobs, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'jobs': page_obj, 'job_count':Job.objects.all().count(), 'jobs': jobs, 'filters': self.filters}
        
        return self.unicorn_render('job_filter.html', context)
