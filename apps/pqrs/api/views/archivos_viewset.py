from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.pqrs.models import ArchivosPqrInformacion, ArchivosPqrRespuesta
from apps.pqrs.api.serializers.archivos_serializer import ArchivoInformacionSerializer, ArchivoRespuestaSerializer
from rest_framework.parsers import JSONParser, MultiPartParser

class ArchivoInformacionViewSet(viewsets.GenericViewSet):
    model = ArchivosPqrInformacion
    serializer_class = ArchivoInformacionSerializer
    parser_classes = (JSONParser, MultiPartParser,)

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_archivos(selfself, request):
        data = ArchivosPqrInformacion.objects.filter(state=True)
        data = ArchivoInformacionSerializer(data, many=True)
        return Response(data.data)

    def list(self, request, *args, **kwargs):
        archivo_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(archivo_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Archivo de informacion para pqr creado satisfactoriamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.serializer_class(data)
            return Response(data.data)
        return Response({'message':'', 'error': 'Archivo de informacion para pqr no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return Response({'message': 'No tiene acceso a esto'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        return Response({'message': 'No tiene acceso a esto'}, status=status.HTTP_401_UNAUTHORIZED)


class ArchivoRespuestaViewSet(viewsets.GenericViewSet):
    model = ArchivosPqrRespuesta
    serializer_class = ArchivoRespuestaSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_archivos(selfself, request):
        data = ArchivosPqrRespuesta.objects.filter(state=True)
        data = ArchivoRespuestaSerializer(data, many=True)
        return Response(data.data)

    def list(self, request, *args, **kwargs):
        archivo_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(archivo_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Archivo de respuesta para pqr creado satisfactoriamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.serializer_class(data)
            return Response(data.data)
        return Response({'message':'', 'error': 'Archivo de respuesta para pqr no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return Response({'message': 'No tiene acceso a esto'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        return Response({'message': 'No tiene acceso a esto'}, status=status.HTTP_401_UNAUTHORIZED)