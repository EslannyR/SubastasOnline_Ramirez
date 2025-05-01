#forms de auctions
from django import forms
from auctions.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Bid

# Obtener el modelo de usuario
User = get_user_model()

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'start_price', 'end_date', 'category', 'image1']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'start_price': 'Precio inicial',
            'end_date': 'Fecha de cierre',
            'category': 'Categoría',
            'image1': 'Imagen 1',
            'image2': 'Imagen 2',
            'image3': 'Imagen 3',
        }
        help_texts = {
            'end_date': 'Formato: día-mes-año hora:minutos',
        }
        widgets = {
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto de tu oferta'}),
        }