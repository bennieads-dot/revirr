# Create your models here.
from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=25, blank=False, default='')
    description = models.CharField(max_length=1500, blank=False, default='')
    company = models.CharField(max_length=25, blank=False, default='')
    submitted_time = models.DateField(auto_now_add=True)
