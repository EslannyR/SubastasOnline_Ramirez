#Librerias necesarias para poder registrar los datos en el archivo json correspondiente
import json
import os

users_db = [] #Se crea una lista vacia para añadir los 9objetos de User

#Se define la clase Users que modela a cada usuario de la plataforma -importante añadir que como es una plataforma de subastas un usuario puede ser tanto vendedor como comprador-.
class Users:
    def __init__(self, user_id, first_name, last_name, address, email, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.password = password
        self.role = None  # Por defecto, más adelante veo su utilidad si incluyo user_admin
        self.bids_per_user = [] #para almacenar las ofertas o pujas de cada usuario

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})" #usuario en texto sencillo

    # metodo paara actualizar dirección en caso de cambio
    def update_address(self, new_address):
        self.address = new_address

    # metodo para registrar una oferta realizada por un usuario - terminar a futuro -
    def make_bid(self, item_id: int, amount: int, bid_date: str):
        bid = {self.user_id, item_id, amount, bid_date}
        self.bids_per_user.append(bid)

# Para cargar los usuarios desde el archivo json
def load_users():
    link = 'TuModeloDeCliente+Ramirez/db_data/users.json'
    if os.path.exists(link): #esto verifica si el archivo existe
        with open(link, 'r') as file:
            try:
                users_db = json.load(file) #si existe lo carga como diccionaripo
            except json.JSONDecodeError:
                users_db = [] #sino lo deja vacio (en caso de error o no existir)
    else:
        users_db = [] #sino lo devuelve vacio
    return users_db

# Para guardar los usuarios en el archivo json
def save_users(users_db):
    link = 'TuModeloDeCliente+Ramirez/db_data/users.json'
    with open(link, 'w') as file:
        json.dump([user.__dict__ for user in users_db], file, indent=4) #convierte a diccionario y lo guarda en el json
