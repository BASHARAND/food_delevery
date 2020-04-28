from tastypie.resources import ModelResource
from .models import Category
from tastypie.authorization import Authorization
class NoteResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'note'
        authorization = Authorization()
