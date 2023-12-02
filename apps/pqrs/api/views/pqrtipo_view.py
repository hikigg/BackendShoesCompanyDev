from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.pqrs.api.serializers.pqrtipo_peticion import PqrTipoPeticion

class PqrTipoPeticionViewSet(viewsets.ModelViewSet):
    serializer_class = PqrTipoPeticion

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
            return Response({'message':'Tipo de peticion para pqr creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            pqr_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if pqr_serializer.is_valid():
                pqr_serializer.save()
                return Response({'message': 'Tipo de peticion para pqr actualizadoa correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': pqr_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({'message': 'Tipo de peticion para pqr elimianda correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe un tipo de peticion para pqr con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

