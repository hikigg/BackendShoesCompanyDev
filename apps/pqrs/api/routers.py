from rest_framework.routers import DefaultRouter
from apps.pqrs.api.views.pqrrespuesta_view import PqrRespuestaViewSet
from apps.pqrs.api.views.pqrinformacion_view import PqrInformacionViewSet
from apps.pqrs.api.views.pqrtipo_view import PqrTipoPeticionViewSet
from apps.pqrs.api.views.archivos_viewset import ArchivoInformacionViewSet, ArchivoRespuestaViewSet

router = DefaultRouter()

router.register(r'informacion', PqrInformacionViewSet, basename='informacion')
router.register(r'archivos_info', ArchivoInformacionViewSet, basename='archivos_info')
router.register(r'respuesta', PqrRespuestaViewSet, basename='respuesta')
router.register(r'archivos_res', ArchivoRespuestaViewSet, basename='archivos_res')
router.register(r'peticion', PqrTipoPeticionViewSet, basename='peticion')

urlpatterns = router.urls