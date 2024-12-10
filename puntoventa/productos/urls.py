# productos/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),  
    path('agregar_producto/', views.agregar_producto, name='agregar_producto')
]
