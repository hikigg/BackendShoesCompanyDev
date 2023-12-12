# from rest_framework import serializers
# from apps.productos.models import ImagenesProducto
#
# class ImagenSerializer(serializers.ModelSerializer):
#
#     def create(self, validated_data):
#         image = validated_data.get('image', None)
#         if image is None:
#             validated_data['image'] = ''  # O un valor predeterminado según tu lógica
#         return ImagenesProducto.objects.create(**validated_data)
#
#     class Meta:
#         model = ImagenesProducto
#         exclude = ('state', 'created_at', 'modified_at', 'deleted_at')
#
#
#     def to_representation(self, instance):
#         return {
#             'id': instance.id,
#             'codigo': instance.codigo,
#             'image': instance.image.url,
#             'producto': instance.producto_id.nombre if instance.producto_id is not None else '',
#         }
