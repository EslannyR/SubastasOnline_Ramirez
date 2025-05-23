from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('mi-perfil/', views.profile_view, name='profile_view'),
    path('cambiar-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('acerca-de-mi/', views.about_view, name='about'),
]
