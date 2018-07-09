from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include

from . import views

urlpatterns = [
    #home
    path('', views.home, name='home'),
    
]