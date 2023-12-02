from rest_framework import serializers
from apps.pqrs.models import PqrRespuesta

class PqrRespuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PqrRespuesta
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'numero_radicado': instance.pqr_id.num_radicado if instance.pqr_id is not None else '',
            'tipo_peticion': instance.peticion_pqr_id.descripcion if instance.peticion_pqr_id is not None else '',
            'descripcion' : instance.descripcion,
            'fecha_respuesta' : instance.fecha_respuesta,
            'local_peticion': instance.local_id.nombre_local if instance.local_id is not None else '',
            'nit_local': instance.local_id.nit_local if instance.local_id is not None else '',
            'nombre_usuario': instance.usuariodatos_id.nombre_usuario if instance.usuariodatos_id is not None else '',
            'apellidos_usuario': instance.usuariodatos_id.apellido_usuario if instance.usuariodatos_id is not None else '',
            'direccion_usuario': instance.usuariodatos_id.direccion_usuario if instance.usuariodatos_id is not None else '',
            'tipo_documento': instance.usuariodatos_id.tipo_documento if instance.usuariodatos_id is not None else '',
            'documento': instance.usuariodatos_id.documento if instance.usuariodatos_id is not None else '',
            'telefono_usuario': instance.usuariodatos_id.telefono_usuario if instance.usuariodatos_id is not None else '',
        }