from rest_framework import serializers
from apps.pqrs.models import ArchivosPqrInformacion, ArchivosPqrRespuesta


class ArchivoInformacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArchivosPqrInformacion
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')


    def create(self, validated_data):
        archivo = validated_data.get('archivos_pqrs', None)
        if archivo is None:
            validated_data['archivos_pqrs'] = ''  # O un valor predeterminado según tu lógica
        return ArchivosPqrInformacion.objects.create(**validated_data)


    def to_representation(self, instance):
        return {
            'id': instance.id,
            'codigo': instance.codigo,
            'archivos' : instance.archivos_pqrs.url if instance.archivos_pqrs is not None else '',
            'num_radicado' : instance.pqr_id.num_radicado if instance.pqr_id is not None else '',
        }


class ArchivoRespuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArchivosPqrRespuesta
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')


    def create(self, validated_data):
        archivo = validated_data.get('archivos_respuesta_pqrs', None)
        if archivo is None:
            validated_data['archivos_respuesta_pqrs'] = ''  # O un valor predeterminado según tu lógica
        return ArchivosPqrRespuesta.objects.create(**validated_data)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'codigo' :instance.codigo,
            'archivos' : instance.archivos_respuesta_pqrs.url if instance.archivos_respuesta_pqrs is not None else '',
            'num_radicado' : instance.pqr_info_id.num_radicado if instance.pqr_info_id is not None else '',
        }

