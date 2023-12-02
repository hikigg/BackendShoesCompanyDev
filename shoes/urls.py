
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.usuarios.api.routers')),
    path('productos/', include('apps.productos.api.routers')),
]
