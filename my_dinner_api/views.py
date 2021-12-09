from re import split
from my_dinner_api.models import Cliente, Platillo, Orden
from my_dinner_api.serializers import ClienteSerializer, PlatilloSerializer, OrdenSerializer
from rest_framework import generics
import pytz, datetime
from rest_framework import status
from rest_framework.response import Response


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PlatilloList(generics.ListCreateAPIView):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer

    def get(self, request, *args, **kwargs):
        if request.data:
            tipo_comida = str(request.data.get('tipo_comida'))[0].upper()
            fecha_inicio = str(request.data.get('fecha_inicio')) + 'T00:00:00'
            fecha_fin = str(request.data.get('fecha_fin')) + 'T23:59:59'
            cantidad_vendida = 0
            ordenes_por_fecha = Orden.objects.filter(timestamp__range=[fecha_inicio, fecha_fin])
            platillos_por_tipo = [platillo.nombre for platillo in Platillo.objects.filter(tipo=tipo_comida)]
            for orden in ordenes_por_fecha:
                for platillo in platillos_por_tipo:
                    if platillo in orden.detalle:
                        detalles = split('\n',orden.detalle)
                        for detalle in detalles:
                            if platillo in detalle:
                                cantidades_con_precio = split(' x',detalle)
                                cantidad = split(' = ',cantidades_con_precio[1])[0]
                                cantidad_vendida += int(cantidad)
            return Response({'Cantidad vendida': cantidad_vendida},status=status.HTTP_200_OK)
            
        return super().get(request, *args, **kwargs)

class PlatilloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer

class OrdenList(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def post(self, request, *args, **kwargs):
        now = datetime.datetime.now(pytz.timezone('America/Mexico_City'))
        opening_time = now.replace(hour=16,minute=0,second=0,microsecond=0)
        closing_time = now.replace(hour=21,minute=0,second=0,microsecond=0)
        if opening_time > now or now > closing_time:
            return Response({'message': 'Working hours are from 16:00 to 21:00.'},status=status.HTTP_423_LOCKED)
        return super().post(request, *args, **kwargs)

class OrdenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
