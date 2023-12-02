from django.db import models
from simple_history.models import HistoricalRecords

class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_at = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    modified_at = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    deleted_at = models.DateField('Fecha eliminacion', auto_now=True, auto_now_add=False)

    def __str__(self):
        pass

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

