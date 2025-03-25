#Librerias necesarias para poder registrar los datos en el archivo json correspondiente
import json
import os

Items_db = [] #Se crea una lista vacia para añadir los 9objetos de items

#Se define la clase Items para modelar a cada item de la plataforma (productos que se van a subastar)
class Items:
    def __init__(self, item_id, title, description, start_price, start_date, end_date, category, seller_id):
        self.item_id = item_id
        self.title = title
        self.description = description
        self.start_price = start_price
        self.start_date = start_date
        self.end_date =end_date
        self.category = category
        self.seller_id = seller_id #este es el id_user, solo que acá el usuario esta modo vendedor

    def __str__(self):
        return f"{self.title} (ID: {self.item_id})" #item en texto sencillo

# Para cargar los items/productos a subastar desde el archivo json
def load_items():
    link = 'TuModeloDeCliente+Ramirez/db_data/items.json'
    if os.path.exists(link):
        with open(link, 'r') as file:
            try:
                items_db = json.load(file)
            except json.JSONDecodeError:
                items_db = []
    else:
        items_db = []
    return items_db

#funcion para guardar los items en el json
def save_items(items_db):
    link = 'TuModeloDeCliente+Ramirez/db_data/items.json'
    with open(link, 'w') as file:
        json.dump([item.__dict__ for item in items_db], file, indent=4)