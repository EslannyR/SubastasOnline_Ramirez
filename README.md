# 🛍 Plataforma de Subastas Online
Alumna: Eslanny Ramírez

Este proyecto consiste en el desarrollo de una **plataforma de subastas online** construida con Django, que permitirá a los usuarios publicar productos, explorarlos, y participar en subastas mediante un sistema de ofertas. La aplicación está basada en el patrón **MVT (Modelo - Vista - Template)** y cuenta con una estructura clara, visual atractiva y funcionalidades esenciales bien organizadas.

---

### 🎯 Objetivos del proyecto

- Implementar una aplicación web funcional, simple y bien estructurada, usando Django como framework principal.
- Permitir a los usuarios registrarse, iniciar sesión y gestionar sus productos publicados.
- Desarrollar un sistema de búsqueda y filtrado eficiente para facilitar la exploración de ítems.
- Construir una base sólida para, en siguientes etapas, permitir a los usuarios ofertar por productos y cerrar subastas automáticamente.
- Aplicar conceptos aprendidos en el curso como herencia de templates, formularios, validaciones, diseño responsivo con Bootstrap y persistencia de datos con modelos.

Este avance representa la base de la plataforma, sobre la cual se integrarán nuevas funcionalidades más adelante, siendo la mas importante:

- Ofertar por un producto.
- Restricción para no ofertar por nuestro propio producto publicado.
- Cierre y ganador de un producto, generando la venta.

---

## 🔍 ¿Cómo probar?

### 1. Iniciar sesión o registrarse
- Al abrir la app, serás dirigido al login.
- Si no tienes cuenta, puedes registrarte fácilmente.
- Se solicita: nombre, apellido, email, dirección, usuario, contraseña.

### 2. Publicar producto
- Menú → **Publicar**
- Completa los campos:
  - Título
  - Descripción
  - Precio inicial
  - Fecha de cierre
  - Categoría (selección)
  - Hasta 3 imágenes (opcional)

### 3. Ver productos publicados
- Menú → **Mis productos**
- Muestra título, estado (Activo o Cerrado), y permite ver detalles.

### 4. Buscar productos publicados
- Menú → **Explorar**
- Verás todos los ítems activos
- Puedes filtrar por:
  - Texto (título o palabra clave)
  - Categoría
  - Rango de precio (mínimo y máximo)

---

## 🎨 Estilo visual

- Paleta de colores suave:
  - Navbar: `#34748c`
  - Botones: `#fbc5c4`
  - Fondo: `#ccdce4`
- Diseño responsive y limpio (modo claro)
- Formularios centrados y bien espaciados

---

## 📁 Estructura de carpetas destacada

```bash
├── auctions/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
        ├── base.html
│       └── auctions/
│           ├── login.html
│           ├── register.html
│           ├── home.html
│           ├── explore_items.html
│           ├── publish_item.html
│           ├── my_items.html
│           ├── filters_form.html
│           └── item_detail.html
