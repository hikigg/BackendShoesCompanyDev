from rest_framework import serializers
from apps.productos.models import Producto
from apps.productos.api.serializers.general_serializers import ( TallasProductoSerializer, CategoriasProductoSerializer, )

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        producto_data = self.get_producto_data(instance)
        return producto_data

    def get_producto_data(self, instance):
        return{
            'id': instance.id,
            'nombre' : instance.nombre,
            'descripcion' : instance.descripcion,
            'marca' : instance.marca,
            'precio' : instance.precio,
            'color' : instance.color,
            'genero' : instance.genero,
            'disponible' : instance.disponible,
            'categoria': instance.categoria_id.descripcion if instance.categoria_id is not None else '',
            'talla': instance.talla_id.descripcion if instance.talla_id is not None else '',
            'local': instance.local_usuario_id.nombre_local if instance.local_usuario_id is not None else '',
        }
