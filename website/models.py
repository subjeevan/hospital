from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField( max_length=50)
    post = models.CharField(max_length=50)
    image = models.ImageField(upload_to='testimonialpic')
    message = models.CharField( max_length=50)

class Contacts(models.Model):
    name =models.CharField(max_length=20)
    email = models.EmailField(max_length=30, default='')
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=100)

class Courses(models.Model):
    c_name = models.CharField(max_length=40)
    teacher = models.CharField(max_length=40)
    duration = models.IntegerField()
    max_student = models.IntegerField()
    fees = models.IntegerField()
    detail = models.CharField(max_length=60,default='')
