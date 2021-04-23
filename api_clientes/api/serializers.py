from rest_framework import serializers
from .models import Tbl_Clientes, Tbl_Enderecos

class Tbl_ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Clientes
        fields = [
            'nome_completo_cliente', 
            'cpf', 
            'email',
            'data_nascimento',
            'numero_telefone',
        ]

class Tbl_EnderecosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Enderecos
        fields = [
            'rua', 
            'numero', 
            'complemento',
            'cep',
            'cidade',
            'estado',
            'pais',
            'cliente',
        ]
        depth = 1