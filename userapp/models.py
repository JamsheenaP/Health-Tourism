from django.db import models
from adminapp.models import Package
# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=15)
    role = models.IntegerField(default=1)

class User (models.Model):
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    dob=models.DateField()
    email=models.EmailField()
    mobile=models.CharField(max_length=15)

class Order(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    package= models.ForeignKey(Package,on_delete=models.CASCADE)
    card_num=models.CharField(max_length=14)
    cvv=models.IntegerField()
    expiry=models.CharField(max_length=7)
    booking_date=models.CharField(max_length=14)
    slots = models.CharField(max_length=10)
    copies = models.IntegerField(default=1)
    amount=models.FloatField()
    order_date=models.DateField(default='2020-01-01')
    status=models.IntegerField()
