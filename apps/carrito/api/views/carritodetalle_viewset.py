from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.carrito.api.serializers.carritodetalle_serializer import CarritoDetalleSerializer
from rest_framework.permissions import AllowAny

class CarritoDetalleViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoDetalleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        carrito_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(carrito_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Detalles de carrito creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        carrito = self.get_queryset().filter(id=pk).first()

        if carrito:
            serializer = self.serializer_class(carrito, data=request.data, partial=True)
            if serializer.is_valid():
                cantidad = serializer.validated_data.get('cantidad')
                precio = serializer.validated_data.get('precio')

                total = serializer.calcular_total(cantidad, precio)  # Recalcular el total

                serializer.validated_data['total'] = total  # Asignar el nuevo total al serializer

                serializer.save()
                return Response({'message': 'Detalles de carrito actualizados correctamente'},
                                status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'No existen detalles de carrito con estos datos'},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        carrito = self.get_queryset().filter(id=pk).first() # get instance
        if carrito:
            carrito.state = False
            carrito.save()
            return Response({'message': 'Detalles de carrito elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existen detalles de carrito con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

