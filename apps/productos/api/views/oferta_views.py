from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.productos.api.serializers.oferta_serializer import OfertaProductoSerializer

class OfertaProductoViewSet(viewsets.ModelViewSet):
    serializer_class = OfertaProductoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        oferta_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(oferta_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Oferta de producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            oferta_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if oferta_serializer.is_valid():
                oferta_serializer.save()
                return Response({'message': 'Oferta de producto actualizado correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': oferta_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        oferta = self.get_queryset().filter(id=pk).first() # get instance
        if oferta:
            oferta.state = False
            oferta.save()
            return Response({'message': 'Oferta de producto elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe una oferta de producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
