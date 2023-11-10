
from django.urls import path, include
from myapp import views
from django.contrib import admin

urlpatterns = [
   
    path('',views.homepage, name='home'),
   
    
]