#Librerias necesarias para poder registrar los datos en el archivo json correspondiente
import json
import os

bids_db = [] #Se crea una lista vacia para añadir los objetos de bids

class Bids:
    def __init__(self, bid_id, user_id, item_id, amount, bid_date):
        self.bid_id = bid_id
        self.user_id = user_id
        self.item_id = item_id
        self.amount = amount
        self.bid_date = bid_date

    def __str__(self):
        return f"Bid ID: {self.bid_id}, User ID: {self.user_id}, Item ID: {self.item_id}, Amount: {self.amount}, Date: {self.bid_date}"

# Cargar bids desde el archivo JSON
def load_bids():
    link = './db_data/bids.json'
    if os.path.exists(link):
        with open(link, 'r') as file:
            try:
                bids_loaded = json.load(file)
            except json.JSONDecodeError:
                bids_loaded = []
    else:
        bids_loaded = []
    return bids_loaded

#Guardar bids en el archivo JSON
def save_bids(bids_db):
    link = './db_data/bids.json'
    os.makedirs(os.path.dirname(link), exist_ok=True)
    with open(link, 'w') as file:
        json.dump([bid.__dict__ for bid in bids_db], file, indent=4)

