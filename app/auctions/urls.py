from django.urls import path
from django.shortcuts import redirect
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('publish_item/', views.publish_item, name='publish_item'),
    path('mis-productos/', views.my_items, name='my_items'),
    path('producto/<int:item_id>/', views.item_detail, name='item_detail'),
    path('explorar/', views.explore_items, name='explore_items'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
