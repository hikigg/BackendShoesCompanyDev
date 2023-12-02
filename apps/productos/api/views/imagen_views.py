from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.productos.api.serializers.imagen_serializer import ImagenSerializer

class ImagenProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ImagenSerializer


    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        imagen_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(imagen_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Imagen de producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            imagen_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if imagen_serializer.is_valid():
                imagen_serializer.save()
                return Response({'message': 'Imagen de producto actualizado correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': imagen_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        imagen = self.get_queryset().filter(id=pk).first() # get instance
        if imagen:
            imagen.state = False
            imagen.save()
            return Response({'message': 'Imagen de producto elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe una imagen de producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
