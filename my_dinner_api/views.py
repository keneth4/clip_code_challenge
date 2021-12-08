from my_dinner_api.models import Cliente, Platillo, Orden
from my_dinner_api.serializers import ClienteSerializer
from rest_framework import generics


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer