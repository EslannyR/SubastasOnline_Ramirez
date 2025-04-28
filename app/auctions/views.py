from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from django.utils import timezone
from .models import Item
from django.utils.timezone import now
import uuid


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

@login_required
def publish_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.code = uuid.uuid4()
            item.save()
            messages.success(request, "¡Producto publicado exitosamente!")
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'auctions/publish_item.html', {'form': form})

@login_required
def my_items(request):
    items = Item.objects.filter(seller=request.user).order_by('-start_date')
    now = timezone.now()
    for item in items:
        item.status = "Activo" if item.end_date > now else "Cerrado"
    return render(request, 'auctions/my_items.html', {'items': items, 'now': now})

def item_detail(request, code):
    item = get_object_or_404(Item, code=code)
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

#Editor de productos cuando este no tiene ofertas
@login_required
def edit_item(request, code):
    item = get_object_or_404(Item, code=code, seller=request.user)

    # Verificar si el producto ya tiene ofertaas
    if item.bids.exists():
        messages.error(request, "No puedes editar este producto porque ya tiene ofertas.")
        return redirect('my_items')

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            # No permitir cambiarr el título, categoría ni fecha de inicio
            form.instance.title = item.title
            form.instance.category = item.category
            form.instance.start_date = item.start_date

            form.save()
            messages.success(request, "Producto editado exitosamente.")
            return redirect('my_items')
    else:
        form = ItemForm(instance=item)

    return render(request, 'auctions/edit_item.html', {'form': form})

#Eliminar mi producto sin ofertas
@login_required
def confirm_delete_item(request, code):
    item = get_object_or_404(Item, code=code, seller=request.user)

    # Verificar si tiene ofertas
    if item.bids.exists():
        messages.error(request, "No puedes eliminar este producto porque ya tiene ofertas.")
        return redirect('my_items')

    if request.method == 'POST':
        item.delete()
        messages.success(request, "Producto eliminado exitosamente.")
        return redirect('my_items')

    return render(request, 'auctions/confirm_delete_item.html', {'item': item})
