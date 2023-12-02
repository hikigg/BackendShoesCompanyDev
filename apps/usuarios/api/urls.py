from django.urls import path

from apps.usuarios.api.views.general_views import RolesViewSet, UsuarioDatosViewSet, LocalUsuarioViewSet
from apps.usuarios.api.views.usuario_viewset import *

urlpatterns = [
    path('roles/',RolesViewSet.as_view(), name = 'roles'),
    path('usuario_datos/', UsuarioDatosViewSet.as_view(), name = 'usuario_datos'),
    path('local/', LocalUsuarioViewSet.as_view(), name = 'local'),
]