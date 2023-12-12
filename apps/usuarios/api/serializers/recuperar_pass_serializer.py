from rest_framework import serializers

class RecuperarPassSerializer(serializers.Serializer):
    email = serializers.EmailField()