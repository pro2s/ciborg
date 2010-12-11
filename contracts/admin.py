from django.contrib import admin
from contracts.models import Contract, Company, Delivery

admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Delivery)