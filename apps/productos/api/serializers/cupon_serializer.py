from rest_framework import serializers
from apps.productos.models import CuponesProducto

class CuponesProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuponesProducto
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'codigo': instance.codigo,
            'descuento': instance.descuento,
            'inicio_oferta': instance.inicio_oferta,
            'fin_oferta': instance.fin_oferta,
            'producto': instance.producto_id.nombre if instance.producto_id is not None else '',

        }