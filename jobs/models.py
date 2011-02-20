#coding: utf-8 
from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    # instrument = models.CharField(max_length=100)

class JobType(models.Model):
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    # instrument = models.CharField(max_length=100)

class Job(models.Model):
    job_type = models.ForeignKey(JobType)
    user = models.ForeignKey(Worker)
    # device = models.ForeignKey(Devices) для связи в будущем с общей базой
    device_name = models.CharField(max_length=100)
    device_number = models.IntegerField()
    job_date = models.DateField()

class MaterialType(models.Model):
    name = models.CharField(max_length=50)
    unit_name = models.CharField(max_length=50)

class Material(models.Model):
    job = models.ForeignKey(Job)
    material_type = models.ForeignKey(MaterialType)
    count = models.IntegerField()

