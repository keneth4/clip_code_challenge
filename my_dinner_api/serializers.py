from re import split
from rest_framework import serializers

from my_dinner_api.models import Cliente, Platillo, Orden

class ClienteSerializer(serializers.Serializer):
    email = serializers.CharField()
    nombre = serializers.CharField()
    domicilio = serializers.CharField()
    telefono = serializers.CharField()

    def create(self, validated_data):
        validated_data['domicilio'] = split(',',validated_data['domicilio'])
        for i,domicilio in enumerate(validated_data['domicilio']):
            if domicilio[0] == ' ': validated_data['domicilio'][i] = domicilio[1:]
            if domicilio[-1] == ' ': validated_data['domicilio'][i] = domicilio[:-1]
        return Cliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.domicilio = validated_data.get('domicilio', instance.domicilio)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance

class PlatilloSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    descripcion = serializers.CharField()
    precio = serializers.FloatField()
    tipo = serializers.ChoiceField(Platillo.TIPO_DE_COCINA)
    estatus = serializers.ChoiceField(Platillo.OPCIONES_DE_ESTATUS)

    def create(self, validated_data):
        return Platillo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.estatus = validated_data.get('estatus', instance.estatus)
        instance.save()
        return instance

class OrdenSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cliente = serializers.CharField()
    timestamp = serializers.DateTimeField()
    total = serializers.FloatField()
    detalle = serializers.CharField()

    def create(self, validated_data):
        return Orden.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.total = validated_data.get('total', instance.total)
        instance.detalle = validated_data.get('detalle', instance.detalle)
        instance.save()
        return instance