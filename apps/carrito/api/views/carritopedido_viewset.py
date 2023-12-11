from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.carrito.api.serializers.carritopedido_serializer import CarritoPedidoSerializer
from apps.carrito.api.serializers.carritodetalle_serializer import CarritoDetalleSerializer
from rest_framework.permissions import AllowAny
from apps.productos.models import Producto

class CarritoPedidoViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoPedidoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()


    def list(self, request, *args, **kwargs):
        carrito_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(carrito_serializer.data, status=status.HTTP_200_OK)

    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'Pedido de carrito creado correctamente'}, status=status.HTTP_201_CREATED)
    #     return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        pedido_serializer = self.serializer_class(data=request.data)
        if pedido_serializer.is_valid():
            pedido = pedido_serializer.save()

            detalles = request.data.get('detalles', [])  # Obtener los detalles del pedido

            for detalle in detalles:
                # Validación de cantidad de productos
                if detalle.get('cantidad', 0) <= 0:
                    return Response({'message': 'La cantidad de productos debe ser mayor que cero'},
                                    status=status.HTTP_400_BAD_REQUEST)

                # Validación de existencia de productos
                producto_id = detalle.get('producto_id')
                producto = Producto.objects.filter(id=producto_id).first()
                if not producto:
                    return Response({'message': f'El producto con ID {producto_id} no existe'},
                                    status=status.HTTP_400_BAD_REQUEST)

                detalle['carrito_id'] = pedido.id  # Asignar el ID del pedido a cada detalle

                cantidad = detalle.get('cantidad')
                precio = detalle.get('precio')

                detalle['total'] = CarritoDetalleSerializer().calcular_total(cantidad,
                                                                             precio)  # Calcular el total para cada detalle

                detalle_serializer = CarritoDetalleSerializer(data=detalle)
                if detalle_serializer.is_valid():
                    detalle_serializer.save()
                else:
                    pedido.delete()  # Eliminar el pedido si hay errores en los detalles
                    return Response({'message': '', 'error': detalle_serializer.errors},
                                    status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Pedido de carrito creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': pedido_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            carrito_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if carrito_serializer.is_valid():
                carrito_serializer.save()
                return Response({'message': 'Pedido de carrito correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': carrito_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        carrito = self.get_queryset().filter(id=pk).first() # get instance
        if carrito:
            carrito.state = False
            carrito.save()
            return Response({'message': 'Pedido de carrito elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existen un pedido de carrito con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

