# -*- coding: utf-8 -*-
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    unn = models.CharField(max_length=12, blank = True)
    rs = models.CharField(max_length=12, blank = True)
    bank = models.CharField(max_length=50, blank = True)
    phone = models.CharField(max_length=10, blank = True)
    director = models.CharField(max_length=30, blank = True)
    acts = models.CharField(max_length=10, blank = True)
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
    
    def __unicode__(self):
        return self.name

class Contract(models.Model):
    number = models.CharField(max_length=30)
    company = models.ForeignKey(Company)
    open_date = models.DateField()
    close_date = models.DateField(blank = True)
    description = models.CharField(max_length=100, blank = True)
    payment_date = models.DateField()
    sum = models.CharField(max_length=30, blank = True)
    is_invoice = models.BooleanField(blank = True)
    parent_id = models.ForeignKey("self", null=True, blank=True)
    class Meta:
        verbose_name = 'Договор (Счет)'
        verbose_name_plural = 'Договора (Счета)'
    
    def __unicode__(self):
        type_string = u'Счет' if self.is_invoice else u'Договор'
        return u'%s %s от %s (%s)' % (type_string, self.number, self.open_date, self.company.name)


class Delivery(models.Model):
    doc_number = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    date = models.DateField()
    contract = models.ForeignKey(Contract)
    is_akt = models.BooleanField(blank = True)
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

    def __unicode__(self):
            type_string = u'Акт' if self.is_akt else u'ТТН(ТН)'
            return u'%s № %s от %s (%s)' % (type_string, self.doc_number, self.date, self.contract.company.name)
