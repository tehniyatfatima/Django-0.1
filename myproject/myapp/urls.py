
from django.urls import path, include
from myapp import views
from django.contrib import admin

urlpatterns = [
   
    path('',views.homepage, name='home'),
    path('password',views.password, name='password'),
    path('signin',views.Signin, name='signin'),
   
    
]