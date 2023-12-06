from rest_framework.routers import DefaultRouter
from apps.carrito.api.views.carritodetalle_viewset import CarritoDetalleViewSet
from apps.carrito.api.views.carritopedido_viewset import CarritoPedidoViewSet

router = DefaultRouter()

router.register(r'detalles', CarritoDetalleViewSet, basename='detalles')
router.register(r'pedido', CarritoPedidoViewSet, basename='pedido')

urlpatterns = router.urls