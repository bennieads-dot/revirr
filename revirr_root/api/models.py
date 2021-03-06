from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50,  blank=False,
                            default='company name')
    city = models.CharField(max_length=25, blank=False, default='')
    street = models.CharField(max_length=25, blank=False, default='')
    description = models.CharField(max_length=50, blank=False, default='')
    logo = models.CharField(max_length=100, blank=False, default='')


class Question(models.Model):
    title = models.CharField(max_length=25, blank=False, default='')
    prompt = models.TextField(blank=False, default='')
    createdAt = models.DateTimeField(auto_now_add=True)
    question_type = models.TextField(
        max_length=10, blank=False, default='code')
    last_updated = models.DateTimeField(auto_now=True)


class Assignment(models.Model):
    name = models.CharField(max_length=25, blank=False, default='')
    time_limit_minutes = models.IntegerField()
    questions = models.ManyToManyField(Question, related_name="questions")


class Job(models.Model):
    title = models.CharField(max_length=25, blank=False, default='')
    description = models.TextField(blank=False, default='')
    company = models.ForeignKey(
        Company, related_name='jobs', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=25, blank=False, default='')
    post_start_date = models.DateTimeField()
    post_end_date = models.DateTimeField()
    remote = models.BooleanField(default=False)
    salary = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    assignment = models.ForeignKey(
        Assignment, related_name='jobs', on_delete=models.SET_NULL, null=True, default=None)
