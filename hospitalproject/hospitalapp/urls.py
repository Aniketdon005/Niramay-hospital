from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    
    path('base',views.base,name = 'base'),
    path('contact',views.contact,name = 'contact'),
    path('userlogout',views.userlogout,name = 'userlogout'),
    path('usersignin',views.usersignin,name = 'usersignin'),
    path('usersignup',views.usersignup,name = 'usersignup'),
    path('paitentdashboard',views.paitentdashboard,name = 'paitentdashboard'),
]
