# -*- coding: utf-8 -*-
from django.db import models

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
    doc_nubmer = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier)
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

class Division(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

class Place(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    floor = models.IntegerField()
    bldg  = models.IntegerField()
    number = models.CharField(max_length=4)
    decsription = models.CharField(max_length=100)
    division = models.ForeignKey(Division)
    class Meta:
        verbose_name = 'Рабочие место'
        verbose_name_plural = 'Рабочие места'

class Set(models.Model):
    decsription = models.CharField(max_length=100)
    
class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    name_value = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    units_name = models.CharField(max_length=20)

class Device(models.Model):
    name = models.CharField(max_length=50)
    inumber = models.CharField(max_length=10)
    snumber = models.CharField(max_length=20)
    value  = models.CharField(max_length=30)
    waranty = models.IntegerField()
    description = models.CharField(max_length=100)
    delivery = models.ForeignKey(Delivery)
    set = models.ForeignKey(Set)
    devicetype = models.ForeignKey(DeviceType)
