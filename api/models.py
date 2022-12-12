from django.db import models

class Motorista(models.Model):
    Cod_Motorista = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)
    Telefone =models.CharField(max_length=20)
    CNH = models.CharField(max_length=20)

class Veiculo(models.Model):
    Placa = models.CharField(primary_key=True,max_length=20)
    Marca = models.CharField(max_length=50)
    Veiculo = models.CharField(max_length=100)
    Km_Troca_Oleo = models.CharField(max_length=50)

class Controle(models.Model):
    controle_ID = models.AutoField(primary_key=True)
    Veiculo = models.ForeignKey('Veiculo',on_delete=models.RESTRICT)
    Motorista = models.ForeignKey('Motorista',on_delete=models.RESTRICT)
    Data_saida = models.DateField(max_length=12)
    Hora_saida = models.TimeField(max_length=20)
    Km_saida   = models.CharField(max_length=20)
    Destino    = models.CharField(max_length=300)
    Data_retorno = models.DateField(max_length=12)
    Hora_retorno = models.TimeField(max_length=20)
    Km_Retorno   = models.CharField(max_length=20)
    Km_percorrido = models.CharField(max_length=20)






