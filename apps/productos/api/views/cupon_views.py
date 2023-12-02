from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.productos.api.serializers.cupon_serializer import CuponesProductoSerializer

class CuponProductoViewSet(viewsets.ModelViewSet):
    serializer_class = CuponesProductoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        cupon_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(cupon_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Cupon de producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            cupon_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if cupon_serializer.is_valid():
                cupon_serializer.save()
                return Response({'message': 'Cupon de producto actualizado correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': cupon_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({'message': 'Cupon de producto elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe un cupon de producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
