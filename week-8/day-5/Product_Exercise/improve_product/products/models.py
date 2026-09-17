from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        LAPTOP = "LAPTOP", "Laptop"
        PHONE = "PHONE", "Phone"
        ACCESSORY = "ACCESSORY", "Accessory"

    name = models.CharField(max_length=100, db_index=True)
    sku = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, default="")
    available_from = models.DateField(blank=True, null=True)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.ACCESSORY,
    )

def __str__(self):
        return self.name