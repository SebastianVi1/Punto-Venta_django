# Punto de Venta Django

Sistema de gestión de ventas e inventario desarrollado con Django.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Características](#características)
- [Modelos de Datos](#modelos-de-datos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Gestión de Usuarios y Roles](#gestión-de-usuarios-y-roles)
- [Pruebas](#pruebas)
- [Créditos](#créditos)
- [Licencia](#licencia)

---

## Descripción

**Punto de Venta Django** es una aplicación web para la gestión de inventario, ventas y usuarios en pequeños y medianos comercios. Permite registrar productos, realizar ventas, generar reportes y administrar usuarios con diferentes roles.

## Características

- **Gestión de productos:** Alta, modificación, eliminación y listado de productos con categorías, precios, stock y descripciones.
- **Inventario:** Visualización y ordenamiento de productos por nombre, precio, categoría o stock.
- **Ventas:** Carrito de compras, cálculo automático de totales, registro de ventas y control de stock.
- **Reporte de ventas:** Visualización de ventas agrupadas, totales, montos pagados y cambios.
- **Gestión de usuarios:** Registro, listado y eliminación de usuarios. Soporte para roles de administrador y usuario estándar.
- **Autenticación:** Inicio y cierre de sesión seguro.
- **Interfaz moderna:** Uso de CSS personalizado y fuentes Montserrat.

## Modelos de Datos

### Producto
- `id_unico` (UUID): Identificador único.
- `categoria` (str): Categoría del producto.
- `nombre` (str): Nombre único.
- `precio` (decimal): Precio unitario.
- `stock` (int): Cantidad disponible.
- `descripcion` (str, opcional): Descripción.

### ReporteVenta
- `venta_id` (int): Identificador de la venta.
- `producto` (FK): Producto vendido.
- `cantidad` (int): Unidades vendidas.
- `precio_unitario` (decimal): Precio por unidad.
- `total_por_producto` (decimal): Total por producto.
- `monto_pagado` (decimal): Monto recibido.
- `cambio` (decimal): Cambio entregado.
- `fecha` (datetime): Fecha y hora de la venta.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <URL-del-repo>
   cd Punto-Venta_django
   ```
2. **Instala dependencias:**
   - Requiere Python 3.12+
   - Instala pipenv si no lo tienes:
     ```bash
     pip install pipenv
     ```
   - Instala los paquetes:
     ```bash
     pipenv install
     ```
3. **Aplica migraciones:**
   ```bash
   pipenv run python puntoventa/manage.py migrate
   ```
4. **Crea un superusuario (opcional, para acceso admin):**
   ```bash
   pipenv run python puntoventa/manage.py createsuperuser
   ```
5. **Ejecuta el servidor:**
   ```bash
   pipenv run python puntoventa/manage.py runserver
   ```

## Uso

- Accede a `http://localhost:8000/` en tu navegador.
- Inicia sesión o regístrate como usuario.
- Navega por el menú lateral para acceder a inventario, ventas, reportes y gestión de usuarios.
- El panel de administración de Django está disponible en `/admin` para superusuarios.

## Gestión de Usuarios y Roles

- **Usuarios estándar:** Pueden iniciar sesión, ver inventario y realizar ventas.
- **Administradores:** Pueden gestionar usuarios, acceder al panel de administración y realizar todas las operaciones.
- El registro de usuarios permite marcar como administrador (`es_admin`).
- Solo superusuarios pueden eliminar otros usuarios.

## Pruebas

- Para ejecutar los tests (si existen):
  ```bash
  pipenv run python puntoventa/manage.py test
  ```
- Se recomienda usar un entorno virtual y base de datos de pruebas.

## Créditos

- Sebastián Villarreal
- Brian Lopez

## Licencia

Este proyecto utiliza la fuente Montserrat bajo la [SIL Open Font License 1.1](https://openfontlicense.org/).

El código fuente está disponible bajo una licencia de software libre. Consulta el repositorio para más detalles.
