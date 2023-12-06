from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.pqrs.api.serializers.pqrespuesta_serializer import PqrRespuestaSerializer
from rest_framework.permissions import IsAuthenticated

class PqrRespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = PqrRespuestaSerializer
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
            return Response({'message':'Respuesta pqr creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            pqr_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if pqr_serializer.is_valid():
                pqr_serializer.save()
                return Response({'message': 'Respuesta respuesta actualizado correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': pqr_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pqr = self.get_queryset().filter(id=pk).first() # get instance
        if pqr:
            pqr.state = False
            pqr.save()
            return Response({'message': 'Respuesta pqr elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe una respuesta pqr con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

