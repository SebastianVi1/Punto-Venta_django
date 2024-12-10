from django.shortcuts import render, redirect
from .models import Producto
from django.db import IntegrityError
from decimal import Decimal
from django.contrib import messages

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html',{'productos': productos})

def products(request):
    return render(request, 'productos/productos.html')


def agregar_producto(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria_producto')
        nombre = request.POST.get('nombre_producto')
        precio = request.POST.get('precio_producto')
        stock = request.POST.get('stock_producto')
        descripcion = request.POST.get('descripcion_productos')

        # Verifica que todos los datos obligatorios estén presentes
        if categoria and nombre and precio and stock:
            try:
                # Convertir precio y stock a tipos numéricos
                precio = Decimal(precio)
                
                stock = int(stock)

                # Crear el producto
                Producto.objects.create(
                    categoria=categoria,
                    nombre=nombre,
                    precio=precio,
                    stock=stock,
                    descripcion=descripcion
                )
                messages.success(request, f" {nombre} agregado correctamente")
                return redirect('products')  # Redirige a la lista de productos

            except IntegrityError:
                # Si el producto ya existe (por nombre)
                mensaje_error = "Este producto ya existe. Por favor, elige otro nombre."
                return render(request, 'productos/productos.html', {'mensaje_error': mensaje_error})

            except ValueError:
                # Si hay un error en la conversión de precio o stock
                mensaje_error = "Por favor, ingresa valores válidos para precio y stock."
                return render(request, 'productos/productos.html', {'mensaje_error': mensaje_error})
        
        else:
            # Si faltan datos obligatorios
            mensaje_error = "Por favor, completa todos los campos obligatorios."
            return render(request, 'productos/productos.html', {'mensaje_error': mensaje_error})

    return render(request, 'productos/products.html')  # Renderiza el formulario de agregar producto