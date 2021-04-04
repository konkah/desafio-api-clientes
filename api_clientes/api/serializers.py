from rest_framework import serializers
from .models import Tbl_Clientes

class Tbl_ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Clientes
        fields = '__all__'

