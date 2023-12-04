from django.contrib import admin
from apps.usuarios.models import *

# Register your models here.

class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_rol')

class LocalUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_local')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

admin.site.register(Roles, RolesAdmin)
admin.site.register(LocalUsuario, LocalUsuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)