from django.urls import path
from apps.carrito.api.views.carritodetalle_viewset import CarritoDetalleViewSet
from apps.carrito.api.views.carritopedido_viewset import CarritoPedidoViewSet

urlpatterns = [
    path('detalles/',  CarritoDetalleViewSet.as_view(), name='detalles'),
    path('pedidos', CarritoPedidoViewSet.as_view(), name='pedidos')
]