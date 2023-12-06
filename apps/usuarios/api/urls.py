from django.urls import path

from apps.usuarios.api.views.general_views import RolesViewSet, LocalUsuarioViewSet
from apps.usuarios.api.views.usuario_sin_views import UsuarioSinAuthViewSet
from apps.usuarios.api.views.local_sin_viewset import LocalUsuarioSinAuthViewSet

urlpatterns = [
    path('roles/',RolesViewSet.as_view(), name = 'roles'),
    path('local/', LocalUsuarioViewSet.as_view(), name = 'local'),
    path('usuario_sin/', UsuarioSinAuthViewSet.as_view(), name = 'usuario_sin' ),
    path('local_sin/', LocalUsuarioSinAuthViewSet.as_view(), name='local_sin')
]