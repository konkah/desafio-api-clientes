from django.db import models

 
class Tbl_Clientes(models.Model):
    nome_completo_cliente = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    numero_telefone = models.CharField(max_length=15)