
from django.db import models
from django.contrib.auth.models import AbstractUser
from owner.models import Customuser


class Driverdetails(models.Model):
    fullname=models.CharField(max_length=20)
    profilepic=models.ImageField(upload_to='images',default=None)
    username=models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='driver_details')
    age=models.IntegerField(blank=True,null=True)
    mobile = models.BigIntegerField(null=True,blank=True)
    email= models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    license_no= models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)

    
class Driverstatus(models.Model):
    name=models.CharField(max_length=20)
    username=models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='driver_status')
    date=models.DateField()
    time=models.TimeField()
    attendance=models.CharField(max_length=20)

class Driverentry(models.Model):
    username=models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='driver_entry')
    vehicleid= models.CharField(max_length=50)
    registration=models.CharField(max_length=15)
    category=models.CharField(max_length=20)
    cc=models.IntegerField()
    date=models.DateField()
    

