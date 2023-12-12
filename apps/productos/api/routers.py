from rest_framework.routers import DefaultRouter
from apps.productos.api.views.general_views import *
from apps.productos.api.views.producto_views import ProductoViewSet
from apps.productos.api.views.oferta_views import OfertaProductoViewSet
# from apps.productos.api.views.imagen_views import ImagenProductoViewSet
from apps.productos.api.views.cupon_views import CuponProductoViewSet
from apps.productos.api.views.productos_sin_autenticacion import ProductoSinAuthViewSet

router = DefaultRouter()

router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'productos_sin', ProductoSinAuthViewSet, basename='productos_sin')
router.register(r'tallas', TallasProductoViewSet, basename='tallas')
router.register(r'ofertas', OfertaProductoViewSet, basename='ofertas')
router.register(r'cupones', CuponProductoViewSet, basename='cupones')
# router.register(r'imagenes', ImagenProductoViewSet, basename='imagenes')
router.register(r'categorias', CategoriasProductoViewSet, basename='categorias')

urlpatterns = router.urls