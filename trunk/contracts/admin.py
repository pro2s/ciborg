from django.contrib import admin
from djprj.contracts.models import Contract, Company, Invoice

admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Invoice)
