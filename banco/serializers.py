from rest_framework import serializers

from banco.models.cliente import Cliente
from banco.models.conta import Conta
from banco.models.extrato import Extrato
from banco.models.transferencia import Transferencia


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Cliente
        fields = "__all__"
class ContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Conta
        fields = "__all__"
class TransferenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Transferencia
        fields = "__all__"
class ExtratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Extrato
        fields = "__all__"

    
