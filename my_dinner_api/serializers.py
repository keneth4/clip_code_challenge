from rest_framework import serializers

from my_dinner_api.models import Cliente, Platillo, Orden

class ClienteSerializer(serializers.Serializer):
    email = serializers.CharField()
    nombre = serializers.CharField()
    domicilio = serializers.CharField()
    telefono = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Cliente.objects.create(**validated_data)