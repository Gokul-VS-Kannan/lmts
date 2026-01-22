
# Create your models here.
from django.db import models
from owner.models import Customuser


class Vehicle(models.Model):
    vehicleid=models.CharField(max_length=50)
    registration=models.CharField(max_length=15)
    category=models.CharField(max_length=20)
    cc=models.IntegerField()
   
class Issue(models.Model):
    user = models.ForeignKey(Customuser, on_delete=models.CASCADE,default=None,related_name='issue')
    vehicleid=models.CharField(max_length=50)
    registration=models.CharField(max_length=15)
    category=models.CharField(max_length=20)
    cc=models.IntegerField()
    complaint=models.CharField(max_length=500)
    date=models.DateField()

class Complaint(models.Model):
    user = models.ForeignKey(Customuser, on_delete=models.CASCADE,default=None,related_name='complaint')
    vehicleid=models.CharField(max_length=50)
    registration=models.CharField(max_length=15)
    category=models.CharField(max_length=20)
    cc=models.IntegerField()
    complaint=models.CharField(max_length=500)
    date=models.DateField()
