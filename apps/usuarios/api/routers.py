from rest_framework.routers import DefaultRouter
from apps.usuarios.api.views.general_views import *
from apps.usuarios.api.views.usuario_viewset import UsuarioViewSet
from apps.usuarios.api.views.usuario_sin_views import UsuarioSinAuthViewSet
from apps.usuarios.api.views.local_sin_viewset import LocalUsuarioSinAuthViewSet

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'usuarios_sin', UsuarioSinAuthViewSet, basename='usuarios_sin')
router.register(r'local_sin', LocalUsuarioSinAuthViewSet, basename='local_sin')
router.register(r'roles', RolesViewSet, basename='roles')
router.register(r'local', LocalUsuarioViewSet, basename='local')


urlpatterns = router.urls