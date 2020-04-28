from django.shortcuts import render
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django import forms
from django.http import HttpResponse
from . import models
from .models import Category
# Create your views here.
def NoteResource1(request):

       product = models.Category.objects.get(id=1)
       context = {
            'product':product,
       }
       return render(request, 'Product.html', context)