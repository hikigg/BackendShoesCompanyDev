from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.usuarios.api.serializers.usuario_serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        pass

    def list(self, request, *args, **kwargs):
        usuario_serializer = self.serializer_class(self.get_queryset().filter(is_active=True), many=True)
        return Response(usuario_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        if self.get_queryset(pk):
            usuario_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response({'message': 'Usuario actualizado correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': usuario_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        usuario = self.get_queryset().filter(id=pk).first() # get instance
        if usuario:
            usuario.is_active = False
            usuario.save()
            return Response({'message': 'Usuario elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe un suuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
