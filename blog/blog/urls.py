"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #1er parametro: es el texto de la url
    #2do parametro: es la vista que se va a ejecutar
    #3er parametro: es el nombre de la url
    path('', views.Home, name='home'),
    path('nosotros/', views.Nosotros, name='nosotros'),
    path('cocina/', views.Cocina, name='cocina'),

    #urls aplicaciones
    path('noticias/', include('apps.noticias.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]