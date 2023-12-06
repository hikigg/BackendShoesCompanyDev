from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.usuarios.api.serializers.usuario_serializer import UsuarioSerializer

class UsuarioSinAuthViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  # Permite el acceso sin autenticación

    def list(self, request, *args, **kwargs):
        usuario_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(usuario_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return Response({'message': 'No tienes acceso a esta seccion'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        return Response({'message': 'No tienes acceso a esta seccion'}, status=status.HTTP_401_UNAUTHORIZED)
