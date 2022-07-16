from rest_framework import serializers

from banco.importacoes import Cliente, Conta, Saldo, Transferencia


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

class SaldoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Saldo
        fields = "__all__"
