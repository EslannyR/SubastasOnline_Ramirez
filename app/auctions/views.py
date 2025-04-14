from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from django.utils import timezone
from .models import Item
from django.utils.timezone import now


@login_required

def home(request):
    now = timezone.now()
    items = Item.objects.filter(end_date__gt=now)

    # Filtros
    search = request.GET.get("search")
    category = request.GET.get("category")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if search:
        items = items.filter(title__icontains=search)
    if category:
        items = items.filter(category=category)
    if min_price:
        items = items.filter(start_price__gte=min_price)
    if max_price:
        items = items.filter(start_price__lte=max_price)

    return render(request, "auctions/home.html", {
        "items": items,
        "categories": Item.CATEGORY_CHOICES
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente al registrarse
            return redirect('home')  # redirige a una vista home
    else:
        form = RegisterForm()
    return render(request, 'auctions/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña inválidos.")
    return render(request, 'auctions/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def publish_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            messages.success(request, "¡Producto publicado exitosamente!")
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'auctions/publish_item.html', {'form': form})

@login_required
def my_items(request):
    items = Item.objects.filter(seller=request.user)
    now = timezone.now()
    for item in items:
        item.status = "Activo" if item.end_date > now else "Cerrado"
    return render(request, 'auctions/my_items.html', {'items': items})

from django.shortcuts import get_object_or_404

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'auctions/item_detail.html', {'item': item})

def explore_items(request):
    items = Item.objects.filter(end_date__gt=timezone.now())
    # Filtros
    search = request.GET.get("search")
    category = request.GET.get("category")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if search:
        items = items.filter(title__icontains=search)
    if category:
        items = items.filter(category=category)
    if min_price:
        items = items.filter(start_price__gte=min_price)
    if max_price:
        items = items.filter(start_price__lte=max_price)

    return render(request, "auctions/explore_items.html", {
        "items": items,
        "categories": Item.CATEGORY_CHOICES
    })

