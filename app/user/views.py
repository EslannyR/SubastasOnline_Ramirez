from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.forms import RegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente al registrarse
            return redirect('home')  # redirige a una vista home
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


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
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
