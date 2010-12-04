from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    unn = models.CharField(max_length=12)
    rs = models.CharField(max_length=12)
    bank = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    director = models.CharField(max_length=30)
    acts = models.CharField(max_length=10)
    def __unicode__(self):
	return self.name
	
class Contract(models.Model):
    number = models.CharField(max_length=30)
    company = models.ForeignKey(Company)
    open_date = models.DateField()
    close_date = models.DateField()
    description = models.CharField(max_length=100)
    sum = models.CharField(max_length=30)

class Invoice(models.Model):
    contract = models.ForeignKey(Contract)
    sum = models.IntegerField()
    payment_date = models.DateField()
    receipt_date = models.DateField()
    
    