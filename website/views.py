from django.shortcuts import render,redirect
from .models import Testimonial,Contacts,Courses
from django.contrib import messages
# Create your views here.

def home(request):
    data = Testimonial.objects.all().order_by()[:3]
    return render(request,'index.html',{'datas':data})

def contact(request):
    if request.method=='POST':
        full_name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=Contacts(name=full_name,email=email,subject=subject,message=message)
        data.save()
        messages.success(request,"Data saved Successfully")
        return redirect('contacts')

    return render(request,'contacts.html')

def about(request):
    return render(request,'about.html')


def courses(request):
    courses=Courses.objects.all()
    return render(request,'courses.html',{'courses':courses})