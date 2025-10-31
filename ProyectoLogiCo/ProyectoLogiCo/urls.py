"""
URL configuration for ProyectoLogiCo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from App.views import index

urlpatterns = [
    path('', views.paginaPrincipal, name='paginaPrincipal'),
    path('farmacias/', views.farmacia_list, name='farmacia_list'),
    path('farmacias/', views.farmacia_list, name='farmacia_list'),
    path('farmacias/crear/', views.farmacia_create, name='farmacia_create'),
    path('farmacias/<int:pk>/editar/', views.farmacia_update, name='farmacia_update'),
    path('farmacias/<int:pk>/eliminar/', views.farmacia_delete, name='farmacia_delete'),
    
    # Moto
    path('motos/', views.moto_list, name='moto_list'),
    path('motos/crear/', views.moto_create, name='moto_create'),
    
    path('motos/<int:pk>/editar/', views.moto_update, name='moto_update'),
    path('motos/<int:pk>/eliminar/', views.moto_delete, name='moto_delete'),
    
    # Motorista
    path('motorista/', views.motorista_list, name='motorista_list'),
    path('motorista/crear/', views.motorista_create, name='motorista_create'),
    path('motorista/<int:pk>/editar/', views.motorista_update, name='motorista_update'),
    path('motorista/<int:pk>/eliminar/', views.motorista_delete, name='motorista_delete'),
]

