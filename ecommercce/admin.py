from django.contrib import admin
from .models import Category,Products,MyImage

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cname']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['pname','price','description','category']

admin.site.register(Products,ProductAdmin)

class MyImageAdmin(admin.ModelAdmin):
    list_display=['name','description','img']
    
admin.site.register(MyImage,MyImageAdmin)
