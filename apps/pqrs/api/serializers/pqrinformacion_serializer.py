from rest_framework import serializers
from apps.pqrs.models import PqrInformacion

class PqrInformacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PqrInformacion
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'numero_radicado' : instance.num_radicado,
            'tipo_peticion': instance.peticion_pqr_id.descripcion if instance.peticion_pqr_id is not None else '',
            'tiempo_restante': instance.tiempo_restante,
            'fecha_estimada': instance.fecha_estimada,
            'local_peticion' : instance.local_id.nombre_local if instance.local_id is not None else '',
            'nombre_usuario' : instance.usuario_id.name if instance.usuario_id is not None else '',
            'apellidos_usuario' : instance.usuario_id.last_name if instance.usuario_id is not None else '',
            'direccion_usuario' : instance.usuario_id.direccion if instance.usuario_id is not None else '',
            'tipo_documento' : instance.usuario_id.tipo_documento if instance.usuario_id is not None else '',
            'documento' : instance.usuario_id.documento if instance.usuario_id is not None else '',
            'telefono_usuario' : instance.usuario_id.telefono if instance.usuario_id is not None else '',
        }