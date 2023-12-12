from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.base.api import GeneralListAPIView
from apps.usuarios.models import LocalUsuario, Roles
from apps.usuarios.api.serializers.general_serializer import  RolesSerializer
from apps.usuarios.api.serializers.local_serializer import LocalUsuarioSerializer

class RolesViewSet(viewsets.GenericViewSet):
    model = Roles
    serializer_class = RolesSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_roles(selfself, request):
        data = Roles.objects.filter(state=True)
        data = RolesSerializer(data, many=True)
        return Response(data.data)

    def list(self, request, *args, **kwargs):
        roles_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(roles_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Rol creado satisfactoriamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.serializer_class(data)
            return Response(data.data)
        return Response({'message':'', 'error': 'Rol no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Rol actualizado satisfactoriamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({'message':'Rol elimiando correctamente'}, status=status.HTTP_200_OK)
        return Response({'message':'', 'error':'Rol no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

class LocalUsuarioViewSet(viewsets.GenericViewSet):
    model = LocalUsuario
    serializer_class = LocalUsuarioSerializer

    @action(detail=False, methods=['get'])
    def get_local(selfself, request):
        data = LocalUsuario.objects.filter(state=True)
        data = LocalUsuarioSerializer(data, many=True)
        return Response(data.data)

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    def list(self, request, *args, **kwargs):
        localusuario_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(localusuario_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Local para usuario creado satisfactoriamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Datos de usuario no encontrados '}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Local de usuario actualizados correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        local_usuario = self.get_queryset().filter(id=pk).first()
        if local_usuario:
            local_usuario.state = False
            local_usuario.save()
            return Response({'message':'Local de usuario eliminado'}, status=status.HTTP_200_OK)
        return Response({'message':'No existe el local de usuario que busca'}, status=status.HTTP_400_BAD_REQUEST)

