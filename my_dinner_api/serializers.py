import pytz, datetime, json
from re import split
from rest_framework import serializers
from my_dinner_api.models import Cliente, Platillo, Orden

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['email', 'nombre', 'domicilio', 'telefono']

    def create(self, validated_data):
        validated_data['domicilio'] = split(',',validated_data['domicilio'])
        for i,domicilio in enumerate(validated_data['domicilio']):
            if domicilio[0] == ' ': validated_data['domicilio'][i] = domicilio[1:]
            if domicilio[-1] == ' ': validated_data['domicilio'][i] = domicilio[:-1]
        return Cliente.objects.create(**validated_data)

class PlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platillo
        fields = ['id', 'nombre', 'descripcion', 'precio', 'tipo', 'estatus']

    def to_internal_value(self, data):
        data['tipo'] = str(data['tipo'])[0].upper()
        data['estatus'] = str(data['estatus'])[0].upper()
        return super().to_internal_value(data)

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ['id', 'cliente', 'timestamp', 'total', 'detalle']

    def to_internal_value(self, data):
        instance = self.instance
        if instance:
            data['cliente'] = instance.cliente.email
            data['timestamp'] = instance.timestamp
        else:
            data['timestamp'] = datetime.datetime.now(pytz.timezone('America/Mexico_City'))
        detalle_orden = json.loads(str(data['detalle']).replace('\'','"'))
        cliente = Cliente.objects.filter(email=data['cliente']).first()
        detalle_str = 'Pedido para ' + cliente.nombre + '\nDirección: ' + json.loads(str(cliente.domicilio).replace('\'','"'))[0] + '\n\n'
        total = 0
        for orden in detalle_orden:
            platillo = Platillo.objects.filter(id=orden['id_platillo']).first()
            subtotal = platillo.precio * orden['cantidad']
            total += subtotal
            detalle_str += platillo.nombre + ' x' + str(orden['cantidad']) + ' = ' + str(subtotal) + '\n'
        detalle_str += '\nTotal = ' + str(total)
        data['detalle'] = detalle_str
        data['total'] = total
        return super().to_internal_value(data)