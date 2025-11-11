############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Step 1: Populate the database with sample products
def populate_products():
    sample_products = [
        {"upc": "12345", "name": "Coffee", "price": 8.32},
        {"upc": "67890", "name": "Muffin", "price": 2.50},
        {"upc": "53964", "name": "Eggs", "price": 7.53},
        {"upc": "24680", "name": "Bread", "price": 3.75},
        {"upc": "97531", "name": "Apple", "price": 1.25},
        {"upc": "64208", "name": "Cookie", "price": 2.15},
        {"upc": "53197", "name": "Juice", "price": 3.45},
    ]


    for p in sample_products:
        Product.objects.get_or_create(
            upc=p["upc"],
            defaults={"name": p["name"], "price": p["price"]}
        )

    print("✅ Database populated with sample products.")


# Step 2: Simulate scanning of a product
def scan_product():
 while True:
        upc = input("\nEnter product UPC (or 'exit' to quit): ").strip()
        if upc.lower() == "exit":
            print("Exiting cash register...")
            break

        try:
            product = Product.objects.get(upc=upc)
            print(f"-> Product found: {product.name} - ${product.price}")
        except Product.DoesNotExist:
            print("❌ Unknown product")


# --- Run the app ---
if __name__ == "__main__":
    populate_products()
    scan_product()