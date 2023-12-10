from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.productos.api.serializers.producto_serializer import ProductoSerializer
from apps.productos.models import Producto
class ProductoSinAuthViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]  # Permite el acceso sin autenticación

    #
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        producto_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(producto_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        return Response({'message': 'No tienes acceso a esta seccion'}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        return Response({'message': 'No tienes acceso a esta seccion'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        return Response({'message': 'No tienes acceso a esta seccion'}, status=status.HTTP_401_UNAUTHORIZED)

