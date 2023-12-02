from django.contrib import admin
from apps.pqrs.models import *

# Register your models here.

class PqrInformacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_radicado')

class PqrRespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class PqrTipoPeticionAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

admin.site.register(PqrInformacion, PqrInformacionAdmin)
admin.site.register(PqrRespuesta, PqrRespuestaAdmin)
admin.site.register(PqrPeticion, PqrTipoPeticionAdmin)