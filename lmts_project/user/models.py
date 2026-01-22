
from django.db import models
from django.contrib.auth.models import AbstractUser
from owner.models import Customuser
# Create your models here.


class Userdetails(models.Model):
    fullname = models.CharField(max_length=20)
    profilepic = models.ImageField(upload_to='images',default=None)
    username = models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='user_details')
    age = models.IntegerField(blank=True,null=True)
    mobile = models.BigIntegerField(blank=True,null=True)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    
  
class Orderdetails(models.Model):
    username = models.ForeignKey(Customuser,on_delete=models.CASCADE,default=None,related_name='order_details')
    material = models.CharField(max_length=30)
    weight = models.IntegerField()
    shipfrom = models.CharField(max_length=255)
    shipto = models.CharField(max_length=255)
    pickdate = models.DateField()
    deliverydate = models.DateField()
    is_approved = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
