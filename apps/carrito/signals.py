# carrito/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.carrito.models import CarritoPedido

@receiver(post_save, sender=CarritoPedido)
def actualizar_detalles_carrito(sender, instance, created, **kwargs):
    if created:  # Verifica si se creó un nuevo CarritoPedido
        detalles_pedido = instance.carrito_id.all()  # Obtener los detalles del carrito relacionados con el pedido
        for detalle in detalles_pedido:
            detalle.state = False  # Cambiar el estado del detalle del carrito a False
            detalle.save()  # Guardar el cambio en el estado
