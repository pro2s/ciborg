# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse
from devices.models import Device, ServiceType, Service, ServiceForm
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.conf import settings
ABOUT = "Раздел управления устройствами и обслуживанием"

def index(request):
    device_list = Device.objects.all()
    t = loader.get_template('devices/index.html')
    c = Context({
    'device_list': device_list,
    'menu': settings.MENU, 'activetag':'index',
    'about': ABOUT
                        })
    return HttpResponse(t.render(c))

def service(request):
    service_list = Service.objects.all()
    form = ServiceForm()

    if request.method == "POST":
            form = ServiceForm(request.POST)
            if form.is_valid():
                form.save()
                # Do something.
    else:
        formset = ServiceForm()
    return render_to_response("devices/service.html", {
        "formset": form,
        'service_list': service_list,
        'menu': settings.MENU, 'activetag':'service',
        'about': ABOUT,
    })


def dev_search(request):
    data = {}
    if request.is_ajax():
		q = request.GET.get( 'q' )
		if q is not None:
			results = Device.objects.filter(inumber__contains = q).order_by( 'name' )
			data = {
				'device_list': results,
        }
    return render_to_response( 'devices/results.html', data)

