from rest_framework import serializers
from apps.carrito.models import CarritoDetalle

class CarritoDetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarritoDetalle
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'cantidad': instance.cantidad,
            'precio': instance.precio,
            'impuesto': instance.impuesto,
            'total': instance.total,
            'producto': instance.producto_id.nombre if instance.producto_id is not None else '',
            'nombre_usuario': instance.usuariodatos_id.nombre_usuario if instance.usuariodatos_id is not None else '',
            'apellidos_usuario': instance.usuariodatos_id.apellido_usuario if instance.usuariodatos_id is not None else '',
            'direccion_usuario': instance.usuariodatos_id.direccion_usuario if instance.usuariodatos_id is not None else '',
            'tipo_documento': instance.usuariodatos_id.tipo_documento if instance.usuariodatos_id is not None else '',
            'documento': instance.usuariodatos_id.documento if instance.usuariodatos_id is not None else '',
            'telefono_usuario': instance.usuariodatos_id.telefono_usuario if instance.usuariodatos_id is not None else '',
            'cupon': instance.cupones_id.codigo if instance.cupones_id is not None else '',
        }
