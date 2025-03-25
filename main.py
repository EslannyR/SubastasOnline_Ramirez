#Se importa las clases y funciones necesarias, incluyendo las funciones de carga y guardado de datos
from packages.users import Users, load_users, save_users
from packages.items import Items, load_items, save_items
import json
import os

#Variables globales***
current_user = {} #este me sirve para guardar el usuerio activo
#lista de objetos cargados y creados
users_db = []
items_db = []
#Para asignar id's unicos
user_id = 1
item_id = 1

# Para cargar los usuarios registrados en el json y los convierto en ojbetos USERS
loaded_users = load_users()
for data in loaded_users:
    user = Users(data['user_id'], data['first_name'], data['last_name'], data['address'], data['email'], data['password'])
    users_db.append(user)
    user_id = max(user_id, user.user_id + 1)

# Para cargar los usuarios registrados en el json y los convierto en ojbetos ITEMS
loaded_items = load_items()
for data in loaded_items:
    item = Items(data['item_id'], data['title'], data['description'], data['start_price'], data['start_date'], data['end_date'], data['category'], data['seller_id'])
    items_db.append(item)
    item_id = max(item_id, item.item_id + 1)

#Funcion para el menú principal, importante, aqui se maneja dos tipos de menú, uno para cuando el usuario inicio sesión y otro para cuando no
def main_menu():
    while True:
        global current_user
        print("\n--- Menú Principal ---")
        if len(users_db) > 0 and current_user:
            print(f"Usuario actual: {current_user.first_name} ({current_user.last_name})")
            print("1. Ver subastas")
            print("2. Hacer una oferta")
            print("3. Ver mis compras")
            print("4. Crear nueva subasta")
            print("5. Actualizar dirección")
            print("6. Cerrar sesión")
        else:
            print("1. Registrar usuario")
            print("2. Iniciar sesión")

        print("0. Salir")

        option = input("Seleccione una opción: ")

        if current_user:
            # Menú para usuarios logueados
            if option == "1":
                view_items()
            elif option == "2":
                make_bid() # - para hacer en el futuro -
            elif option == "3":
                view_purchases() # - para hacer en el futuro -
            elif option == "4":
                create_item()
            elif option == "5":
                new_address()
            elif option == "6":
                current_user = None
                print("✅ Sesión cerrada correctamente.")
            elif option == "0":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("⚠️ Opción no válida. Intente nuevamente.")
        else:
            # Menú para usuarios no logueados
            if option == "1":
                register()
            elif option == "2":
                login()
            elif option == "0":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("⚠️ Opción no válida. Intente nuevamente.")

#Funciones de registro de usuarios nuevos
def register():
    global user_id
    print("\n--- Registro de Usuario ---")
    first_name = input("Nombre: ")
    last_name = input("Apellido: ")
    address = input("Dirección: ")
    email = input("Email: ")
    password = input("Contraseña: ")

    # toma los datos y los guarda
    user = Users(user_id, first_name, last_name, address, email, password)
    users_db.append(user)
    user_id += 1

    save_users(users_db) #guarda en json
    print(f"✅ Registro exitoso. Bienvenido {user.first_name} {user.last_name}")

#Funciones de inicio de sesión
def login():
    global current_user
    print("\n--- Login de Usuario ---")
    email = input("Email: ")
    password = input("Contraseña: ")

    #busca si el usuario y la contraseña son correctos
    for item in users_db:
        if email == item.email and password == item.password:
            current_user = item
            print(f"✅ Inicio de sesión exitoso. Bienvenido {current_user.first_name} {current_user.last_name}")
            return
    print("❌ Usuario o contraseña incorrecta.\n")

#modifica y guarda la direccion nueva del usuario en el json
def new_address():
    global current_user
    print("\n--- Actualización de Direccion ---")
    print(f"Dirección actual: {current_user.address}")
    new_address = input("Ingrese su nueva direccion: ")
    current_user.update_address(new_address)
    save_users(users_db)
    print("✅ Direccion actualizada exitosamente.")

#para crear una nueva subasta ingresando el producto a subastar
def create_item():
    global current_user, item_id, items_db

    print("\n--- Creación de Producto para Subasta ---")
    item_id += 1
    title = input("Nombre del producto: ")
    description = input("Descripción: ")
    start_price = float(input("Precio de inicio: "))
    start_date = input("Fecha de inicio (YYYY-MM-DD): ")
    end_date = input("Fecha de finalización (YYYY-MM-DD): ")
    category = input("Categoría: ")
    seller_id = current_user.user_id

    # - para futuro: crear mensaje de error de dato, reintentar la creation item -

    item = Items(item_id, title, description, start_price, start_date, end_date, category, seller_id)
    items_db.append(item)
    save_items(items_db)
    print(f"✅ Producto creado exitosamente. ID de la Subasta: {item.item_id}")

#para ver los productos en subasta - futuro ver una mejor forma de mostrarlos-
def view_items():
    global items_db
    items_list = items_db

    if not items_list:
        print("⚠️ No hay productos en subasta aún.")
        return

    print("\n--- Productos en Subasta ---")
    for item in items_list:
        print(f"ID: {item.item_id}")
        print(f"Nombre: {item.title}")
        print(f"Descripción: {item.description}")
        print(f"Precio inicial: ${item.start_price}")
        print(f"Vendedor ID: {item.seller_id}")
        print(f"Categoría: {item.category}")
        print(f"Fecha inicio: {item.start_date}")
        print(f"Fecha fin: {item.end_date}\n")

main_menu()