from django.contrib import admin
from django.urls import path
from myenv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('portpolio/', views.port,),
    path('about/', views.about),
    path('services/', views.ser),
    path('contact/', views.contact),
    path('forms/', views.forms)
]
