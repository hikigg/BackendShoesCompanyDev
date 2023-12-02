from rest_framework import serializers
from apps.usuarios.models import Usuario
from apps.usuarios.api.serializers.general_serializer import RolesSerializer, UsuarioDatosSerializer

class UsuarioSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        image = validated_data.get('image', None)
        if image is None:
            validated_data['image'] = ''  # O un valor predeterminado según tu lógica
        return Usuario.objects.create(**validated_data)


    class Meta:
        model = Usuario
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at', 'is_staff', 'is_superuser', 'is_active', 'groups', 'last_login', 'user_permissions')

    # Otros métodos y campos de serializer

    def to_representation(self, instance):
        user_data = self.get_user_data(instance)
        user_data['datos_usuario'] = self.get_user_details(instance)
        user_data['datos_local'] = self.get_local_details(instance)
        return user_data

    def get_user_data(self, instance):
        return {
            'id': instance.id,
            'email': instance.email,
            'image': instance.image if instance.image else None,
            'rol' : instance.roles_id.nombre_rol if instance.roles_id is not None else '',
            'created_at' : instance.created_at
        }

    def get_user_details(self, instance):
        if instance.usuariodatos_id:
            user_details = {
                'nombre': instance.usuariodatos_id.nombre_usuario,
                'apellido': instance.usuariodatos_id.apellido_usuario,
                'direccion': instance.usuariodatos_id.direccion_usuario,
                'telefono': instance.usuariodatos_id.telefono_usuario,
                'tipo_documento': instance.usuariodatos_id.tipo_documento,
            }
            return user_details
        return {}

    def get_local_details(self, instance):
        if instance.locales_usuarios.exists():
            local_details = {}
            local_data = instance.locales_usuarios.first()
            local_details['nombre_local'] = local_data.nombre_local
            local_details['direccion_local'] = local_data.direccion_local
            local_details['telefono_local'] = local_data.telefono_local
            local_details['nit'] = local_data.nit_local
            return local_details
        return {}
