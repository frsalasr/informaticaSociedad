from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include

from . import views

urlpatterns = [
    #home
    path('', views.home, name='home'),
	path('accounts/', include('django.contrib.auth.urls')),

    path('login/', views.login, name='login'),

    
    path('buscador/', views.buscador, name='buscador'),
    path('buscador/<int:id_transaccion>', views.buscar, name='buscar'),

    path('crear/', views.crearTransaccion, name='crear'),

    path('transacciones/', views.transacciones, name='transacciones'),

]