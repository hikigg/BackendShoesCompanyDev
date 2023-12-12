from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
from apps.usuarios.models import Usuario
from apps.productos.models import Producto, CuponesProducto


class CarritoDetalle(BaseModel):
    cantidad = models.PositiveSmallIntegerField()
    precio = models.TextField('Precio de articulos', max_length=10, blank=False, null=False)
    impuesto = models.TextField('Impuesto de articulos', max_length=10, blank=False, null=False)
    total = models.TextField('Total de articulos', max_length=12, blank=False, null=True)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Oferta de articulos', null=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Datos del usuario para los articulos', null=True)
    cupones_id = models.ForeignKey(CuponesProducto, on_delete=models.CASCADE, verbose_name='Cupon de articulos', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return str(self.cantidad)

    class Meta:
        verbose_name = 'Detalle de carrito'
        verbose_name_plural = 'Detalles de Carrito'

class CarritoPedido(BaseModel):
    codigo = models.TextField('Codigo de pedido', max_length=10, blank=False, null=False)
    fecha_pedido = models.DateField('Fecha de pedido', auto_now=True, auto_now_add=False)
    carrito_id = models.ManyToManyField(CarritoDetalle, verbose_name='Articulos pedido', related_name='pedidos')
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Datos del usuario para el pedido', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return str(self.codigo)


    class Meta:
        verbose_name = 'Pedido de carrito'
        verbose_name_plural = 'Pedidos de carrito'