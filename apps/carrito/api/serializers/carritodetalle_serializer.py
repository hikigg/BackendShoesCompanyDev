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
            'nombre_usuario': instance.usuario_id.name if instance.usuario_id is not None else '',
            'apellidos_usuario': instance.usuario_id.last_name if instance.usuario_id is not None else '',
            'direccion_usuario': instance.usuario_id.direccion if instance.usuario_id is not None else '',
            'tipo_documento': instance.usuario_id.tipo_documento if instance.usuario_id is not None else '',
            'documento': instance.usuario_id.documento if instance.usuario_id is not None else '',
            'telefono_usuario': instance.usuario_id.telefono if instance.usuario_id is not None else '',
            'cupon': instance.cupones_id.codigo if instance.cupones_id is not None else '',
        }
