from django.db import models

# Represents one product in the local database (REQ9)
class Product(models.Model):
    upc = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"


