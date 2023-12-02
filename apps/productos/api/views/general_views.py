from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.productos.models import CategoriasProducto, TallasProducto
from apps.productos.api.serializers.general_serializers import CategoriasProductoSerializer, TallasProductoSerializer

class CategoriasProductoViewSet(viewsets.GenericViewSet):
    model = CategoriasProducto
    serializer_class = CategoriasProductoSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_categorias(self, request):
        data = CategoriasProducto.objects.filter(state = True)
        data = CategoriasProductoSerializer(data, many=True)
        return Response(data.data)


    def list(self, request, *args, **kwargs):
        categoria_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(categoria_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Categoria creada satisfactoriamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.serializer_class(data)
            return Response(data.data)
        return Response({'message':'', 'error': 'Categoria no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Categoria actualizada correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({'message':'Categoria eliminada correctamente'}, status=status.HTTP_200_OK)
        return Response({'message':'', 'error': 'Categoria no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

class TallasProductoViewSet(viewsets.GenericViewSet):
    model = TallasProducto
    serializer_class = TallasProductoSerializer


    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_tallas(selfself, request):
        data = TallasProducto.objects.filter(state=True)
        data = TallasProductoSerializer(data, many=True)
        return Response(data.data)

    def list(self, request, *args, **kwargs):
        tallas_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(tallas_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Talla creada satisfactoriamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.serializer_class(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Talla no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Talla actualizada correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({'message':'Talla elimianda correctamente'}, status=status.HTTP_200_OK)
        return Response({'message':'', 'error':'Talla no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
