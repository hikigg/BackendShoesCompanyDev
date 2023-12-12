from rest_framework import serializers
from apps.usuarios.models import LocalUsuario, Roles, Usuario

class LocalUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalUsuario
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def create(self, validated_data):
        # Obtener el local_role
        local_role = Roles.objects.get(nombre_rol='local')

        # Crear el objeto LocalUsuario
        local = LocalUsuario.objects.create(**validated_data)

        # Obtener el usuario asociado al local
        usuario = local.usuario_id

        # Si se encuentra el usuario y su rol es cliente, cambiarlo al rol local
        if usuario and usuario.roles_id.nombre_rol == 'cliente':
            usuario.roles_id = local_role
            usuario.save()

        return local
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre_local,
            'direccion': instance.direccion_local,
            'nit': instance.nit_local,
            'image': instance.image.url if instance.image and hasattr(instance.image, 'url') else '',
            'telefono': instance.telefono_local,
            'nombre_usuario': instance.usuario_id.name if instance.usuario_id is not None else '',
            'apellidos_usuario': instance.usuario_id.last_name if instance.usuario_id is not None else '',
            'documento': instance.usuario_id.documento if instance.usuario_id is not None else '',
            'rol': instance.usuario_id.roles_id.nombre_rol if instance.usuario_id is not None else '',
        }