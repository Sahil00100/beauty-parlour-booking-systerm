from distutils.command.upload import upload
from django.db import models
from django.conf import settings
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#mobiles
class Product(models.Model):
    g=(
        ('male','male'),
        ('female','female'),
    )
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,choices=g)
    
    
    def __str__(self):
        return self.name
    

#order``
class Order(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    product=models.ForeignKey(Product,models.CASCADE)
    mobile_no=models.CharField(max_length=10)
    date=models.DateField(auto_now=False)
    time=models.TimeField(auto_now=False)

class Gallery(models.Model):

    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    
    

    