# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from djprj.ciborg.models import Device

def index(request):
    device_list = Device.objects.all()
    t = loader.get_template('ciborg/index.html')
    c = Context({
    'device_list': device_list,
                        })
    return HttpResponse(t.render(c))

