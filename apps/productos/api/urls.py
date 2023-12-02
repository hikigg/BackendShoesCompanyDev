from django.urls import path
from apps.productos.api.views.general_views import TallasProductoViewSet, CategoriasProductoViewSet
from apps.productos.api.views.cupon_views import CuponProductoViewSet
from apps.productos.api.views.producto_views import *
from apps.productos.api.views.imagen_views import ImagenProductoViewSet
from apps.productos.api.views.oferta_views import OfertaProductoViewSet

urlpatterns = [
    path('tallas/', TallasProductoViewSet.as_view(), name = 'tallas'),
    path('categorias/', CategoriasProductoViewSet.as_view(), name = 'categorias'),
    path('imagen/', ImagenProductoViewSet.as_view(), name = 'imagen'),
    path('oferta/', OfertaProductoViewSet.as_view(), name = 'oferta'),
    path('cupon', CuponProductoViewSet, name = 'cupon'),
]