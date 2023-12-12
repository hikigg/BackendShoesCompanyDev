from rest_framework import serializers
from apps.carrito.models import CarritoDetalle

class CarritoDetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarritoDetalle
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def calcular_total(self, cantidad, precio):
        return cantidad * precio  # Realiza el cálculo del total

    def validate(self, data):
        cantidad = data.get('cantidad')
        precio = data.get('precio')
        impuesto = data.get('impuesto')

        if not cantidad or not precio or not impuesto:
            raise serializers.ValidationError("Todos los campos ('cantidad', 'precio', 'impuesto') son requeridos.")

        # Realiza otras validaciones si es necesario...

        return data

    def create(self, validated_data):
        cantidad = validated_data.get('cantidad')
        precio = validated_data.get('precio')
        impuesto = validated_data.get('impuesto')

        total = self.calcular_total(cantidad, precio) + float(impuesto)  # Calcula el total

        validated_data['total'] = total  # Asigna el total al validated_data

        carrito_detalle = CarritoDetalle.objects.create(**validated_data)
        return carrito_detalle

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'cantidad': instance.cantidad,
            'precio': instance.precio,
            'impuesto': instance.impuesto,
            'total': instance.total,
            'producto': instance.producto_id.nombre if instance.producto_id is not None else '',
            'producto_id': instance.producto_id.id if instance.producto_id is not None else '',
            'nombre_usuario': instance.usuario_id.name if instance.usuario_id is not None else '',
            'apellidos_usuario': instance.usuario_id.last_name if instance.usuario_id is not None else '',
            'direccion_usuario': instance.usuario_id.direccion if instance.usuario_id is not None else '',
            'tipo_documento': instance.usuario_id.tipo_documento if instance.usuario_id is not None else '',
            'documento': instance.usuario_id.documento if instance.usuario_id is not None else '',
            'telefono_usuario': instance.usuario_id.telefono if instance.usuario_id is not None else '',
            'cupon': instance.cupones_id.codigo if instance.cupones_id is not None else '',
        }
