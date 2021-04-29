from rest_framework import serializers
from .models import Tbl_Clientes, Tbl_Enderecos
from validate_docbr import CPF

class Tbl_ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Clientes
        fields = [
            'id',
            'nome_completo_cliente', 
            'cpf', 
            'email',
            'data_nascimento',
            'numero_telefone',
            'deletado',
        ]
    
class Tbl_EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Enderecos
        fields = [
            'id',
            'rua', 
            'numero', 
            'complemento',
            'cep',
            'cidade',
            'estado',
            'pais',
            'cliente',
            'deletado',
        ]
        depth = 1
    
    def validate_cliente_id(self, cli_id):
        cliente = Tbl_Clientes.objects.get(pk = cli_id)
        if cliente.deletado:
            raise serializers.ValidationError(
                'Cliente inexistente.'
            )
        return cli_id