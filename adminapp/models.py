from django.db import models

class Places(models.Model):
    place = models.CharField(max_length=50)
    status = models.IntegerField(default=1)  # 0-disabled 1-enabled

class District(models.Model):
    district_name = models.CharField(max_length=20)
    status = models.IntegerField(default=1)  # 0-disabled 1-enabled

class Category(models.Model):
    category = models.CharField(max_length=20)
    status = models.IntegerField(default=1) #0-disabled 1-enabled

class Package(models.Model):
    title = models.CharField(max_length=50)
    place = models.ForeignKey(Places,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.FloatField()
    no_packages = models.IntegerField()
    sold_package = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images',default='images/img1.jpg')
    description=models.CharField(max_length=1000,default="")
    itin = models.CharField(max_length=1000,default="")


