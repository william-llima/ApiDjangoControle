from rest_framework import serializers
from api.models import Veiculo,Motorista,Controle

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Veiculo
        fields=('__all__')

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Motorista
        fields=('__all__')

class ControleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Controle
        fields=('__all__')



