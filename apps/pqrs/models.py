from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
from apps.usuarios.models import LocalUsuario, UsuarioDatos
from datetime import timedelta
from django.utils import timezone

class PqrPeticion(BaseModel):
    descripcion = models.CharField('Tipo de peticion', max_length=20, blank=False, null=True,unique=True)
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
        verbose_name = 'Tipo peticion pqr'
        verbose_name_plural = 'Tipos peticiones pqrs'

class PqrInformacion(BaseModel):

    def upload_to_pqrs(instance, filename):
        return f"archivos_pqrs/{instance.peticion_pqr_id}/{filename}"

    def get_fecha_estimada_default():
        # Retorna la fecha actual más 14 días
        return timezone.now() + timedelta(days=14)

    num_radicado = models.PositiveIntegerField('Número de Radicado', unique=True)
    peticion_pqr_id = models.ForeignKey(PqrPeticion, on_delete=models.CASCADE, verbose_name='Tipo peticion pqr', null=True, default=1)
    descripcion = models.TextField('Descripcion peticion', max_length=255, blank=False, null=True, unique=True)
    tiempo_restante = models.DateField('Fecha de timepo restante', auto_now=False, auto_now_add=True)
    fecha_estimada = models.DateField('Fecha de estimada', default=get_fecha_estimada_default)
    archivos_pqrs = models.FileField(upload_to=upload_to_pqrs)
    local_id = models.ForeignKey(LocalUsuario, on_delete=models.CASCADE, verbose_name='Local para la peticion', null=True)
    usuariodatos_id = models.ForeignKey(UsuarioDatos, on_delete=models.CASCADE, verbose_name='Datos del usuario para la peticion', null=True)
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return str(self.num_radicado)

    class Meta:
        verbose_name = 'Pqr informacion'
        verbose_name_plural = 'Pqrs informacion'

class PqrRespuesta(BaseModel):

    def upload_to_respuesta_pqrs(instance, filename):
        return f"archivos_respuesta_pqrs/{instance.peticion_pqr_id}/{filename}"

    peticion_pqr_id = models.ForeignKey(PqrPeticion, on_delete=models.CASCADE, verbose_name='Tipo peticion pqr', default=1)
    descripcion = models.TextField('Descripcion respuesta a peticion', max_length=255, blank=False, null=True, unique=True)
    fecha_respuesta = models.DateField('Fecha de respuesta', auto_now=True, auto_now_add=False)
    archivos_respuesta_pqrs = models.FileField(upload_to=upload_to_respuesta_pqrs)
    local_id = models.ForeignKey(LocalUsuario, on_delete=models.CASCADE, verbose_name='Local para la respuesta', null=True)
    usuariodatos_id = models.ForeignKey(UsuarioDatos, on_delete=models.CASCADE, verbose_name='Datos del usuario para la peticion', null=True)
    pqr_id = models.ForeignKey(PqrInformacion, on_delete=models.CASCADE, verbose_name='Pqr informacion de respuesta')
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
        verbose_name = 'Pqr respuesta'
        verbose_name_plural = 'Pqrs respuesta'

