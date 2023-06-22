import json
import os
from django.conf import settings

DATA_FILE = os.path.join(settings.BASE_DIR, 'data', 'products.json')

def get_products():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_products(products):
    with open(DATA_FILE, 'w') as file:
        json.dump(products, file, indent=4)