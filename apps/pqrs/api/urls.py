from django.urls import path
from apps.pqrs.api.views.pqrrespuesta_view import PqrRespuestaViewSet
from apps.pqrs.api.views.pqrinformacion_view import PqrInformacionViewSet
from apps.pqrs.api.views.pqrtipo_view import PqrTipoPeticionViewSet
from apps.pqrs.api.views.archivos_viewset import ArchivoInformacionViewSet, ArchivoRespuestaViewSet


urlpatterns = [
    path('informacion/', PqrInformacionViewSet.as_view(), name = 'informacion'),
    path('respuesta/', PqrRespuestaViewSet.as_view(), name = 'respuesta'),
    path('peticion/', PqrTipoPeticionViewSet.as_view(), name='peticion'),
    path('archivos_info/', ArchivoInformacionViewSet.as_view(), name='archivos_info'),
    path('archivos_res/', ArchivoRespuestaViewSet.as_view(), name='archivos_res'),
]
