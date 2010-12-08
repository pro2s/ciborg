# -*- coding: utf-8 -*-
from django.db import models
from django import forms 
from django.forms import ModelForm, DateField
from datetime import date

class Supplier(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
    class Admin:
	list_display = ('name', 'phone','city')
    def __unicode__(self):
            return '%s (%s)' % (self.name, self.phone) 

class Delivery(models.Model):
    doc_number = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier)
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
    class Admin:
	list_display = ('doc_number', 'date')
    def __unicode__(self):
            return '%s - %s (%s)' % (self.doc_number, self.date, self.supplier.name)

class Division(models.Model):
    name = models.CharField(max_length=30)
    phone  = models.CharField(max_length=10)
    chief  = models.CharField(max_length=50)
    parent = models.ForeignKey('self')
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
    def __unicode__(self):
            return '%s - %s' % (self.name, self.chief)

class Place(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    floor = models.IntegerField()
    building  = models.IntegerField()
    number = models.CharField(max_length=4)
    decsription = models.CharField(max_length=100)
    division = models.ForeignKey(Division)
    class Meta:
        verbose_name = 'Рабочие место'
        verbose_name_plural = 'Рабочие места'
    def __unicode__(self):
            return '%s - %s (%s)' % (self.name, self.phone, self.division.name)

class Set(models.Model):
    decsription = models.CharField(max_length=100)
    place = models.ForeignKey(Place)
    class Meta:
        verbose_name = 'Комплект'
        verbose_name_plural = 'Комплекты'
    
class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    name_value = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    units_name = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Типы устройств'
    def __unicode__(self):
            return '%s - %s' % (self.name, self.icon)

    def __unicode__(self):
            return self.name


class Device(models.Model):
    name = models.CharField(max_length=50)
    inumber = models.CharField(max_length=10, null = True)
    snumber = models.CharField(max_length=20, null = True)
    value  = models.CharField(max_length=30)
    waranty = models.IntegerField()
    description = models.CharField(max_length=100)
    delivery = models.ForeignKey(Delivery, null = True)
    set = models.ForeignKey(Set, null = True)
    devicetype = models.ForeignKey(DeviceType)

    def __unicode__(self):
	if self.inumber != '':
	    return self.inumber
	else:
	    return self.snumber


class ServiceType(models.Model):
    name  = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Тип обслуживания'
        verbose_name_plural = 'Типы обслуживания'
    class Admin:
	list_display = ('name')
    def __unicode__(self):
            return '%s' % (self.name) 

class Service(models.Model):
    device = models.ForeignKey(Device)
    servicetype = models.ForeignKey(ServiceType)
    replace = models.ForeignKey(Device, related_name='replace_device_id', null = True, blank = True)
    description = models.CharField(max_length=50)
    date = models.DateField(default = date.today())


class ServiceForm(ModelForm):
    date = DateField(input_formats=('%d.%m.%Y',),label='', initial=date.today())

    class Meta:
        model = Service
        

#class ServiceForm(forms.Form):
#    device = forms.ModelChoiceField(queryset=Device.objects.all())
#    description = forms.CharField(max_length=50)
#    date = forms.DateField()
#    replace = forms.ModelChoiceField(queryset=Device.objects.all())
#    servicetype = forms.ModelChoiceField(queryset=ServiceType.object.all())

