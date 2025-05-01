# 🛍 Plataforma de Subastas Online
**Alumna: Eslanny Karin Ramírez Sandoval**

Este proyecto consiste en el desarrollo de una **plataforma de subastas online** construida con Django, que permite a los usuarios publicar productos, explorarlos y participar en subastas mediante un sistema de ofertas.

La aplicación está basada en el patrón **MVT (Modelo - Vista - Template)** y cuenta con una estructura modular, diseño visual atractivo y funcionalidades esenciales bien organizadas.

---

## 🎯 Objetivos del proyecto

- Aplicar los conocimientos del curso creando una aplicación web funcional y bien estructurada con Django.
- Permitir a los usuarios registrarse, iniciar sesión y gestionar su perfil.
- Permitir a los usuarios publicar productos, editarlos o eliminarlos (siempre que no tengan ofertas).
- Implementar un sistema de subastas con lógica de ofertas válidas, cierre automático y asignación de ganador.
- Incorporar filtros de búsqueda que faciliten la navegación.
- Aplicar herencia de templates, validaciones de formularios, persistencia con modelos y diseño responsivo con Bootstrap.

Este avance representa una **versión sólida y funcional de la plataforma**, dejando la puerta abierta a futuras mejoras como:
- Confirmación de compra tras el cierre de subasta
- Sistema de mensajería comprador-vendedor
- Notificaciones

---

## 🧪 ¿Cómo probar la app?

### 1. Iniciar sesión o registrarse
- Al ingresar, serás dirigido automáticamente al login.
- Puedes crear una cuenta completando:
  - Nombre, Apellido, Email, Dirección, Nombre de usuario, Contraseña

### 2. Publicar un producto
- Desde el menú superior → **Publicar**
- Completar:
  - Título (solo texto)
  - Descripción
  - Precio inicial
  - Fecha de cierre (date/time)
  - Categoría (selección)
  - Imagen (1 por ahora)

### 3. Explorar productos
- Menú → **Explorar**
- Puedes:
  - Ver los productos activos
  - Filtrar por texto, categoría, precio mínimo/máximo
  - Ver el detalle y ofertar si estás logueado

### 4. Gestionar mis productos
- Menú → **Mis productos**
- Verás el estado del producto (Activo / Cerrado / Con ofertas)
- Si no tiene ofertas, puedes editar o eliminar

### 5. Ofertar por productos
- En la vista de detalle de producto:
  - Verás la oferta más alta (si existe)
  - Si estás logueado, podrás ofertar (si no eres el dueño)
  - No puedes ofertar por debajo del precio inicial ni de la oferta más alta

### 6. Ver mis ofertas
- Menú → **Mis ofertas**
- Podrás ver:
  - Tus ofertas en subastas activas
  - Tus ofertas en subastas cerradas con el resultado (Ganaste / Perdiste)

### 7. Gestionar perfil
- Menú → **Mi perfil**
- Puedes:
  - Ver y editar tus datos (excepto contraseña desde aquí)
  - Cambiar tu contraseña desde una vista personalizada
  - No puedes eliminar tu cuenta si tienes productos u ofertas activas

### 8. Módulo de Cierre y Compra
- Cierre automático de subasta al alcanzar la fecha de cierre.
- En "Mis Productos", se puede ver a quién se vendió el producto.
- En "Mis Ofertas", si el usuario ganó, se le muestra el contacto del vendedor.

### 9. Página “Acerca de mí”
- Vista estática con tu presentación personal y reflexión del proyecto

---

## 🎨 Estilo visual

- Paleta de colores personalizada:
  - Navbar: `#34748c`
  - Botones / acento: `#fbc5c4`
  - Fondos suaves: `#235060`
  - Fondo general: `#ccdce4`
- Estilo limpio, responsivo, con formularios centrados
- Diseño minimalista coherente en todas las páginas

---

## ⚙️ Aspectos técnicos

- Separación por apps: `auctions`, `user`
- Uso de decoradores: `@login_required`
- Formulario con subida de imagen
- Manejo de errores: página 404 personalizada con estilo
- Vista de cambio de contraseña con diseño propio
- Validación personalizada para campos únicos como email
- Eliminación condicional de ítems (no se puede eliminar si hay ofertas)

---
## ⚙️ Instalación y configuración

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/plataforma_subastas.git
cd plataforma_subastas
```

2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
```

3. Instala los requerimientos:

```bash
pip install -r requirements.txt
```

4. Ejecuta las migraciones y levanta el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

---

## 📁 Estructura de carpetas destacada

```bash
├── auctions/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── 404.html
│       └──auctions/
│           ├── home.html
│           ├── explore_items.html
│           ├── filters_form.html
│           ├── item_detail.html
│           ├── my_items.html
│           ├── publish_item.html
│           ├── offer_item.html
├── user/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── user/
│           ├── login.html
│           ├── register.html
│           ├── profile.html
│           ├── change_password.html
│           └── about.html

---

## 🎥 Video de demostración

🔗 [Enlace al video de presentación](https://drive.google.com/file/d/1ZzLaltu0iw_64yCOoalD5TTKHdZAu42r/view?usp=sharing)

---

¡Gracias por revisar mi proyecto! 😊