from django.contrib import admin
from apps.carrito.models import *

# Register your models here.

class CarritoDetallesAdmin(admin.ModelAdmin):
    list_display = ('id', 'cantidad')

class CarritoPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo')

admin.site.register(CarritoDetalle, CarritoDetallesAdmin)
admin.site.register(CarritoPedido, CarritoPedidoAdmin)