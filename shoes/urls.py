
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from apps.usuarios.api.views.views import Login, Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('usuarios/', include('apps.usuarios.api.routers')),
    path('docs/', include_docs_urls(title='Documentacion API')),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('productos/', include('apps.productos.api.routers')),
    path('pqrs/', include('apps.pqrs.api.routers')),
    path('carrito/', include('apps.carrito.api.routers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)