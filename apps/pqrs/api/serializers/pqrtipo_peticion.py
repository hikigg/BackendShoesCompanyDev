from rest_framework import serializers
from apps.pqrs.models import PqrPeticion

class PqrTipoPeticion(serializers.ModelSerializer):

    class Meta:
        model = PqrPeticion
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')
