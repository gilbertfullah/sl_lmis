from django.db import models

class DownloadDocument(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    document = models.FileField(upload_to='documents/')
    download_url = models.URLField()
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return
