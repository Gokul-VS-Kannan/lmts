from django.db import models
from django.contrib.auth.models import AbstractUser
from owner.models import Customuser

class Mechdetails(models.Model):
    fullname = models.CharField(max_length=20)
    profilepic = models.ImageField(upload_to='images',default=None)
    username = models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='mech_details')
    age = models.IntegerField(blank=True,null=True)
    mobile = models.BigIntegerField(blank=True,null=True)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    skill = models.CharField(max_length=500)
    is_approved = models.BooleanField(default=False)

    
class Mechstatus(models.Model):
    name = models.CharField(max_length=20)
    username = models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='mech_status')
    date = models.DateField()
    time = models.TimeField()
    attendance = models.CharField(max_length=20)

class Approvedservice(models.Model):
    username = models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='approved_service')
    vehicleid = models.CharField(max_length=50)
    registration = models.CharField(max_length=15)
    category = models.CharField(max_length=20)
    cc = models.IntegerField()
    complaint = models.CharField(max_length=500)
    date = models.DateField()

class Service(models.Model):
    username = models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='mech_service')
    vehicleid = models.CharField(max_length=50)
    registration = models.CharField(max_length=15)
    category = models.CharField(max_length=20)
    cc = models.IntegerField()
    complaint = models.CharField(max_length=500)   
    service = models.CharField(max_length=500)
    service_date = models.DateField()
    delivery_date = models.DateField()