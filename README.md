# PlataformaSubastasOnlgine

Alumna: Eslanny Ramírez

# 🛍 Plataforma de Subastas Online

Proyecto desarrollado como avance del curso, aplicando el patrón **MVT (Modelo-Vista-Template)** con Django, junto con formularios, búsquedas, herencia de templates y diseño personalizado.

---

## ✅ Requisitos del avance

- [x] Proyecto Web Django con patrón MVT
- [x] Herencia de HTML (`base.html`)
- [x] Al menos 3 clases en models (`User`, `Item`, `Bid`, `Purchase`)
- [x] Un formulario de registro (modelo `User`)
- [x] Un formulario para publicar productos (modelo `Item`)
- [x] Formulario de búsqueda por palabra clave, categoría y rango de precio
- [x] Estilo visual unificado con Bootstrap 5 + paleta de colores personalizada

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
- Footer fijo al final de página

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
