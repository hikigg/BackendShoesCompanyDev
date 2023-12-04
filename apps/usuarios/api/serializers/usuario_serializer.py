from rest_framework import serializers
from apps.usuarios.models import Usuario
from apps.usuarios.api.serializers.general_serializer import RolesSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'name', 'last_name')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'password': instance.password,
            'email': instance.email,
            'image': instance.image if instance.image else None,
            'rol': instance.roles_id.nombre_rol if instance.roles_id is not None else '',
            'nombre_usuario': instance.name,
            'apellido_usuario':instance.last_name,
            'direccion_usuario': instance.direccion,
            'telefono_usuario':instance.telefono,
            'tipo_documento': instance.tipo_documento,
            'documento_identidad': instance.documento,
            'nombre_local': instance.locales_usuarios.nombre_local if instance.locales_usuarios is not None else '',
            'direccion_local': instance.locales_usuarios.direccion_local if instance.locales_usuarios is not None else '',
            'nit_local': instance.locales_usuarios.nit_local if instance.locales_usuarios is not None else '',
            'telefono_local': instance.locales_usuarios.telefono_local if instance.locales_usuarios is not None else '',
        }

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        exclude = (
        'state', 'created_at', 'modified_at', 'deleted_at', 'groups', 'last_login', 'user_permissions')

    def create(self, validated_data):
        image = validated_data.get('image', None)
        if image is None:
            validated_data['image'] = ''  # O un valor predeterminado según tu lógica
        return Usuario.objects.create(**validated_data)

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        update_usuario = super().update(instance, validated_data)
        update_usuario.set_password(validated_data['password'])
        update_usuario.save()
        return update_usuario

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass