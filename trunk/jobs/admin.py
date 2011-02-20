from ciborg.jobs.models import Job, JobType, Material, MaterialType, Worker
from django.contrib import admin

admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(Material)
admin.site.register(MaterialType)
admin.site.register(Worker)