from django.db import models
from productos.models import Producto
from django.contrib.auth.views import LoginView
# Create your models here


class ReporteVenta(models.Model):
    venta_id = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total_por_producto = models.DecimalField(max_digits=10, decimal_places=2)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cambio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha = models.DateTimeField(auto_now_add=True)


class CustomLoginView(LoginView):
    template_name = 'login.html'