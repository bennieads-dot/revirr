# Generated by Django 4.0.3 on 2022-03-29 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_assignment_company_remove_job_submitted_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='post_start_Date',
            new_name='post_start_date',
        ),
    ]