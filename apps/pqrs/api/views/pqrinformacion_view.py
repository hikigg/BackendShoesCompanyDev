from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.pqrs.api.serializers.pqrinformacion_serializer import PqrInformacionSerializer
from rest_framework.permissions import IsAuthenticated

class PqrInformacionViewSet(viewsets.ModelViewSet):
    serializer_class = PqrInformacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        pqr_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(pqr_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Pqr creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    #Actualizar no esta disponible ni eliminar
    def update(self, request, pk=None):
        return Response({'message': 'La acción de actualización no está permitida'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        pqr = self.get_queryset().filter(id=pk).first() # get instance
        if pqr:
            pqr.state = False
            pqr.save()
            return Response({'message': 'Pqr elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe un pqr con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
