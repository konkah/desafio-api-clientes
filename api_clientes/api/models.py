from django.db import models

 
class Tbl_Clientes(models.Model):
    nome_completo_cliente = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    numero_telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_completo_cliente

class Tbl_Enderecos(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    cliente = models.ForeignKey(Tbl_Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.rua + ', ' + self.numero