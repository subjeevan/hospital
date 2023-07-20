from django.contrib import admin
from .models import Testimonial,Contacts,Courses
# Register your models here.

@admin.register(Testimonial)
class Testimonialadmin(admin.ModelAdmin):
    list_display=['name','post','image','message']

@admin.register(Contacts)
class Contactadmin(admin.ModelAdmin):
    list_display=['name','email','message']


@admin.register(Courses)
class Contactadmin(admin.ModelAdmin):
    list_display=['c_name','fees','detail']