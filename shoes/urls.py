
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v1',
      description="Documentacion de api para ShoesCompany",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shoescompany@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.usuarios.api.routers')),
    path('productos/', include('apps.productos.api.routers')),
    path('pqrs/', include('apps.pqrs.api.routers'))
]
