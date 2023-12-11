from django.apps import AppConfig

class CarritoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.carrito'

    def ready(self):
        import apps.carrito.signals