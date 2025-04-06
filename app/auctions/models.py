from django.db import models
from django.contrib.auth.models import AbstractUser

# Extendemos el modelo de usuario si necesitas roles personalizados
class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    bids_per_user = models.PositiveIntegerField(default=0)  # Campo extra opcional

    def __str__(self):
        return f"{self.username} ({self.role})"


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.CharField(max_length=50)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items_published')

    def __str__(self):
        return self.title


class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.item.title}"


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchase')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.title} bought by {self.buyer.username}"
