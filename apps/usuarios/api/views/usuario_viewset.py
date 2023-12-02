from rest_framework import status
from rest_framework import viewsets
from apps.usuarios.models import Usuario
from rest_framework.response import Response
from apps.usuarios.api.serializers.usuario_serializer import UsuarioSerializer, UsuarioListaSerializer

class UsuarioViewSet(viewsets.GenericViewSet):
    model = Usuario
    serializer_class = UsuarioSerializer
    lista_serializer_class = UsuarioListaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request, *args, **kwargs):
        usuarios = self.get_queryset()
        usuario_serializer = self.lista_serializer_class(usuarios, many=True)
        return Response(usuario_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

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
            usuario.state = False
            usuario.save()
            return Response({'message': 'Usuario elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe un suuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
