from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
     path('home',views.index,name='home'),
     path('contact',views.contact,name='contact'),
     path('signup',views.signup,name='signup'),
     
]
