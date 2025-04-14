from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from .models import Item

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nombre', max_length=30, required=True)
    last_name = forms.CharField(label='Apellido', max_length=30, required=True)
    address = forms.CharField(label='Dirección', widget=forms.Textarea, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'start_price', 'end_date', 'category', 'image1', 'image2', 'image3']
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
