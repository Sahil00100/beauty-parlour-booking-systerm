from django.contrib import admin
from django.urls import path,include

from index.views import *

from django.conf.urls.static import static
from django.conf import settings
import os


urlpatterns = [
   
   path('booking/<str:id>/',booking_view,name='booking'),
   path('index/',index_view,name='index'),
   path('register/',register_view,name='register'),
   path('login/',login_view,name='login'),
   path('logout/',logout_view,name='logout'),
   path('orders/',orders_view,name='orders'),
   path('checkout/<str:id>/',checkout_view,name='checkout'),
   path('service/',searvice_view,name='service'),
   path('gallery/',gallery_view,name='gallery'),
  
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
