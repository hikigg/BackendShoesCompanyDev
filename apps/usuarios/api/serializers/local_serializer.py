from rest_framework import serializers
from apps.usuarios.models import LocalUsuario

class LocalUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalUsuario
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre_local,
            'direccion': instance.direccion_local,
            'nit': instance.nit_local,
            'image' : instance.image.url if instance.image is not None else '',
            'telefono': instance.telefono_local,
        }