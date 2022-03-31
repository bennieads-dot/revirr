# Generated by Django 4.0.3 on 2022-03-31 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_job_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='assignment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='api.assignment'),
        ),
    ]
