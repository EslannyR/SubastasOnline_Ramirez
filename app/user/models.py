from django.db import models
from django.contrib.auth.models import AbstractUser

# Extendemos el modelo de usuario si necesitas roles personalizados
class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=[('buyer', 'Buyer'), ('seller', 'Seller')], null=True, blank=True)
    bids_per_user = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.role})"