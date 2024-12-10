from django.db import models
import uuid
# Create your models here.
class Producto(models.Model):
    id_unico = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    categoria = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre