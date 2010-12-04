# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from djprj.ciborg.models import Device, ServiceType, Service, ServiceForm
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.forms import ModelForm

def index(request):
    device_list = Device.objects.all()
    t = loader.get_template('ciborg/index.html')
    c = Context({
    'device_list': device_list,
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
    return render_to_response("ciborg/service.html", {
        "formset": form,
        'service_list': service_list,
    })


