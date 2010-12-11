from devices.models import Division, Place, ServiceType, Device, Service, DeviceType
from django.contrib import admin


admin.site.register(Division)
admin.site.register(Place)
admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(ServiceType)
admin.site.register(Service)

