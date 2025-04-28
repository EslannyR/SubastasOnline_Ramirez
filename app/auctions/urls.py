from django.urls import path
from django.shortcuts import redirect
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('home/', views.home, name='home'),
    path('publish_item/', views.publish_item, name='publish_item'),
    path('mis-productos/', views.my_items, name='my_items'),
    path('producto/<str:code>/', views.item_detail, name='item_detail'),
    path('explorar/', views.explore_items, name='explore_items'),
    path('editar/<str:code>/', views.edit_item, name='edit_item'),
    path('eliminar/<str:code>/', views.confirm_delete_item, name='confirm_delete_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
