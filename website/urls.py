from django.urls import path
from .views import home,about,contact,courses

urlpatterns = [
    path('home/',home,name='home'),
    path('contact/',contact,name='contacts'),
    path('about/',about,name='about'),
    path('courses/',courses,name='courses'),
]
