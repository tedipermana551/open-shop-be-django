from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    shop = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    picture = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)