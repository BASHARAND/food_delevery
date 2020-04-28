from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=30)
    state=models.IntegerField(default=1)
    def __str__(self):
        return self.category
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=15)

    description = models.TextField(max_length= 300,blank=True,null=True)
    state = models.IntegerField(default=1)
    Price = models.IntegerField(default=15)
    count=models.IntegerField(default=100)
    image = models.FileField(upload_to=' Profile_image', blank=True,null=True)
    def __str__(self):
        return self.name
class delevery(models.Model):
    name=models.CharField(blank=False,max_length= 15)
    Phone = models.CharField(max_length=15, null=True)
    def __str__(self):
        return str(self.name)

class Order(models.Model):
    delevery = models.ForeignKey(delevery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # table_num = models.ForeignKey(Table,on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(blank=True, null=True, default=0)
    long_position = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    lat_position = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    delevery = models.CharField(blank=True, null=True, max_length=14)
    delevery_num = models.CharField(blank=True, null=True, max_length=14)
    delevery_date = models.DateField(null=True)
    Phone = models.CharField(max_length=15, null=True)
    Adrress = models.CharField(max_length=200, null=True)
    state_pay = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
class Get(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE , null=True)
    count= models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

# Create your models here.
