from django.contrib import admin
from apps.productos.models import *

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class OfertasProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')

class CategoriasProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class TallasProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class ImagenesProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')

class CuponesProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo')

admin.site.register(Producto, ProductosAdmin)
admin.site.register(OfertasProducto, OfertasProductoAdmin)
admin.site.register(ImagenesProducto, ImagenesProductoAdmin)
admin.site.register(TallasProducto, TallasProductoAdmin)
admin.site.register(CuponesProducto, CuponesProductoAdmin)
admin.site.register(CategoriasProducto, CategoriasProductoAdmin)