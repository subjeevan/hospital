from django.urls import path
from registration.views import homepage,aboutus,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage,name='home'),
    path('contact/',contact,name='contact'),
    path('aboutus/',aboutus,name='about'),
]
