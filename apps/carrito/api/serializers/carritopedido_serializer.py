from rest_framework import serializers
from apps.carrito.models import CarritoPedido


class CarritoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoPedido
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'codigo': instance.codigo,
            'fecha_pedido': instance.fecha_pedido,
            'cantidad': instance.carrito_id.cantidad if instance.carrito_id is not None else '',
            'precio': instance.carrito_id.precio if instance.carrito_id is not None else '',
            'impuesto': instance.carrito_id.impuesto if instance.carrito_id is not None else '',
            'total': instance.carrito_id.total if instance.carrito_id is not None else '',
            'producto': instance.producto_id.nombre if instance.producto_id is not None else '',
            'nombre_usuario': instance.usuariodatos_id.nombre_usuario if instance.usuariodatos_id is not None else '',
            'apellidos_usuario': instance.usuariodatos_id.apellido_usuario if instance.usuariodatos_id is not None else '',
            'direccion_usuario': instance.usuariodatos_id.direccion_usuario if instance.usuariodatos_id is not None else '',
            'tipo_documento': instance.usuariodatos_id.tipo_documento if instance.usuariodatos_id is not None else '',
            'documento': instance.usuariodatos_id.documento if instance.usuariodatos_id is not None else '',
            'telefono_usuario': instance.usuariodatos_id.telefono_usuario if instance.usuariodatos_id is not None else '',
            'cupon': instance.cupones_id.codigo if instance.cupones_id is not None else '',
        }
