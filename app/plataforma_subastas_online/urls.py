
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auctions.urls')),
    path('user/', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 👇 Esto va al final
def custom_404(request, exception):
    from django.shortcuts import render
    return render(request, '404.html', status=404)

handler404 = 'plataforma_subastas_online.urls.custom_404'
