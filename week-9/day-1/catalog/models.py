from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        BOOKS = 'BK', 'Books'
        ELECTRONICS = 'EL', 'Electronics'
        HOME = 'HM', 'Home & Kitchen'

    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=2, choices=Category.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['category', 'is_active'], name='product_cat_active_idx'),
        ]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(price__gte=0),
                name='price_non_negative',
            ),
            models.CheckConstraint(
                condition=models.Q(stock__gte=0),
                name='stock_non_negative',
            ),
        ]

    def __str__(self):
        return self.name

    def is_available(self):
        return self.is_active and self.stock > 0

    def inventory_value(self):
        return self.price * self.stock