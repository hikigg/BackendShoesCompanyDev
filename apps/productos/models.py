from django.db import models
from apps.base.models import BaseModel
from apps.usuarios.models import LocalUsuario
from simple_history.models import HistoricalRecords


class CategoriasProducto(BaseModel):

    descripcion = models.TextField('Descripcion categoria', max_length=30, blank=False, null=True, unique=True)
    local_usuario_id = models.ForeignKey(LocalUsuario, on_delete=models.CASCADE, verbose_name='Local del usuario', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'

class TallasProducto(BaseModel):
    descripcion = models.TextField('Talla de producto', max_length=2, blank=False, null=True, unique=True)
    local_usuario_id = models.ForeignKey(LocalUsuario, on_delete=models.CASCADE, verbose_name='Local del usuario', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Talla de Producto'
        verbose_name_plural = 'Tallas de Producto'

class  Producto(BaseModel):
    nombre = models.CharField('Nombre de producto', max_length=150, unique=True, blank=False, null=False)
    descripcion = models.TextField('Descripcion de Producto', max_length=200, blank=False, null=False)
    precio = models.TextField('Precio de Producto', max_length=10, blank=False, null=False)
    color = models.CharField('Color de producto', max_length=30, unique=True, blank=False, null=False)
    marca = models.CharField('Marca de producto', max_length=20, unique=True, blank=False, null=False)
    genero = models.CharField('Genero de producto', max_length=15, unique=True, blank=False, null=False)
    disponible = models.PositiveSmallIntegerField()
    talla_id = models.ForeignKey(TallasProducto, on_delete=models.CASCADE, verbose_name='Talla de producto', null=True)
    categoria_id = models.ForeignKey(CategoriasProducto, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null=True)
    local_usuario_id = models.ForeignKey(LocalUsuario, on_delete=models.CASCADE, verbose_name='Local del usuario', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return f'{self.nombre} {self.precio}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class ImagenesProducto(BaseModel):
    image = models.ImageField('Imagen de producto', upload_to='perfil/', max_length=255, null=True, blank = True)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = 'Imagen de Producto'
        verbose_name_plural = 'Imagenes de Productos'

class OfertasProducto(BaseModel):
    tipo = models.TextField('Tipo de oferta', max_length=50, blank=False, null=False)
    descuento = models.TextField('Descuento de oferta', max_length=10, blank=False, null=False)
    inicio_oferta = models.DateField('Fecha de inicio oferta', auto_now=True, auto_now_add=False)
    fin_oferta =  models.DateField('Fecha de fin oferta', auto_now=True, auto_now_add=False)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Oferta de producto', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Oferta de producto'
        verbose_name_plural = 'Ofertas de producto'

class CuponesProducto(BaseModel):
    codigo = models.TextField('Codigo de Cupon', max_length=10, blank=False, null=False)
    descuento = models.TextField('Descuento de Cupon', max_length=10, blank=False, null=False)
    inicio_oferta = models.DateField('Fecha de inicio cupon', auto_now=True, auto_now_add=False)
    fin_oferta = models.DateField('Fecha de fin cupon', auto_now=True, auto_now_add=False)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Cupon de producto', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Cupon de producto'
        verbose_name_plural = 'Cupones de producto'

