from django.contrib import admin
from .models import Company, Question, Assignment, Job
# Register your models here.

admin.site.register(Company)
admin.site.register(Question)
admin.site.register(Assignment)
admin.site.register(Job)
