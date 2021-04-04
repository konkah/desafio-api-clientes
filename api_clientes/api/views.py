from django.shortcuts import render
from .models import Tbl_Clientes
from .serializers import Tbl_ClientesSerializer
from rest_framework import viewsets


class Tbl_ClientesViewSet(viewsets.ModelViewSet):
    queryset = Tbl_Clientes.objects.all()
    serializer_class = Tbl_ClientesSerializer
