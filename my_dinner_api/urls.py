"""my_dinner_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from my_dinner_api.views import ClienteList, ClienteDetail, PlatilloDetail, PlatilloList, OrdenDetail, OrdenList

urlpatterns = [
    path('cliente', ClienteList.as_view(), name='clientes'),
    path('cliente/<str:pk>', ClienteDetail.as_view(), name='cliente'),
    path('platillo', PlatilloList.as_view(), name='platillos'),
    path('platillo/<int:pk>', PlatilloDetail.as_view(), name='platillo'),
    path('orden', OrdenList.as_view(), name='ordenes'),
    path('orden/<int:pk>', OrdenDetail.as_view(), name='orden'),
]
