from rest_framework import serializers
from apps.usuarios.models import Roles, LocalUsuario

class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

