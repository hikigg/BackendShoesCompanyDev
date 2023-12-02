from rest_framework import serializers
from apps.productos.models import TallasProducto, CategoriasProducto, CuponesProducto, OfertasProducto

class TallasProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TallasProducto
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

class CategoriasProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriasProducto
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')
