from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import uuid

class Item(models.Model):
    code =models.CharField(max_length=10, unique=True, editable=False, default=uuid.uuid4().hex[:10].upper())
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    CATEGORY_CHOICES = [
        ('electronica', 'Electrónica'),
        ('ropa', 'Ropa y accesorios'),
        ('hogar', 'Hogar y muebles'),
        ('juguetes', 'Juguetes y hobbies'),
        ('herramientas', 'Herramientas y construcción'),
        ('vehiculos', 'Vehículos y repuestos'),
        ('arte', 'Arte y coleccionables'),
        ('libros', 'Libros y papelería'),
        ('deportes', 'Deportes y aire libre'),
        ('otros', 'Otros'),
    ]
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items_published')
    image1 = models.ImageField(upload_to='items/', null=True, blank=True)
    image2 = models.ImageField(upload_to='items/', null=True, blank=True)
    image3 = models.ImageField(upload_to='items/', null=True, blank=True)
    STATUS_CHOICES = [
    ('Activo', 'Activo'),
    ('Cerrado', 'Cerrado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Activo')

    def __str__(self):
        return self.title


class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids_made')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder.username} ofertó ${self.amount} por {self.item.title}"


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchase')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.title} bought by {self.buyer.username}"


