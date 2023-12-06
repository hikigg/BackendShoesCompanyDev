from django.urls import path
from apps.productos.api.views.general_views import TallasProductoViewSet, CategoriasProductoViewSet
from apps.productos.api.views.cupon_views import CuponProductoViewSet
from apps.productos.api.views.productos_sin_autenticacion import ProductoSinAuthViewSet
from apps.productos.api.views.imagen_views import ImagenProductoViewSet
from apps.productos.api.views.oferta_views import OfertaProductoViewSet

urlpatterns = [
    path('tallas/', TallasProductoViewSet.as_view(), name = 'tallas'),
    path('categorias/', CategoriasProductoViewSet.as_view(), name = 'categorias'),
    path('imagen/', ImagenProductoViewSet.as_view(), name = 'imagen'),
    path('oferta/', OfertaProductoViewSet.as_view(), name = 'oferta'),
    path('cupon', CuponProductoViewSet.as_view(), name = 'cupon'),
    path('productos_sin', ProductoSinAuthViewSet.as_view(), name = 'productos_sin'),
]