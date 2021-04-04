from rest_framework import serializers
from .models import Tbl_Clientes, Tbl_Enderecos

class Tbl_ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Clientes
        fields = '__all__'

class Tbl_EnderecosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Enderecos
        fields = '__all__'