from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.productos.api.serializers.producto_serializer import ProductoSerializer
from apps.productos.models import Producto
class ProductoSinAuthViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]  # Permite el acceso sin autenticación

    queryset = Producto.objects.filter(state=True)  # Define el queryset para mostrar solo productos activos

    def list(self, request, *args, **kwargs):
        producto_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(producto_serializer.data, status=status.HTTP_200_OK)
