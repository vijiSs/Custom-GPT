from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now=True)
