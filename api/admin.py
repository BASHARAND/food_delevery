from django.contrib import admin
from . models import Product, Order, Get,Category,delevery

admin.site.register(Product)
admin.site.register(Get)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(delevery)

# Register your models here.
