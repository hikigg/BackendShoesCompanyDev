from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.productos.api.serializers.producto_serializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        producto_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(producto_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if producto_serializer.is_valid():
                producto_serializer.save()
                return Response({'message': 'Producto actualizado correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': producto_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        producto = self.get_queryset().filter(id=pk).first() # get instance
        if producto:
            producto.state = False
            producto.save()
            return Response({'message': 'Producto elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
