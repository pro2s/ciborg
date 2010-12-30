# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse
from devices.models import Contract, Company, Delivery
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.conf import settings
ABOUT = "Раздел управления договорами"

def index(request):
    contracts_list = Contract.objects.all()
    t = loader.get_template('contracts/index.html')
    c = Context({
    'contracts_list': contracts_list,
    'about': ABOUT,
    'menu': settings.MENU, 'activetag':'contracts',
                        })
    return HttpResponse(t.render(c))