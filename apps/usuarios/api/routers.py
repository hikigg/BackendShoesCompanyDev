from rest_framework.routers import DefaultRouter
from apps.usuarios.api.views.general_views import *
from apps.usuarios.api.views.usuario_viewset import UsuarioViewSet

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'roles', RolesViewSet, basename='roles')
router.register(r'usuario-datos', UsuarioDatosViewSet, basename='usuario_datos')
router.register(r'local', LocalUsuarioViewSet, basename='local')

urlpatterns = router.urls