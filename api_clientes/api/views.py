from django.shortcuts import render
from .models import Tbl_Clientes, Tbl_Enderecos
from .serializers import Tbl_ClientesSerializer, Tbl_EnderecosSerializer
from rest_framework import viewsets


class Tbl_ClientesViewSet(viewsets.ModelViewSet):
    queryset = Tbl_Clientes.objects.all()
    serializer_class = Tbl_ClientesSerializer

class Tbl_EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Tbl_Enderecos.objects.all()
    serializer_class = Tbl_EnderecosSerializer