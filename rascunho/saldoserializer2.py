
# from banco.importacoes import Saldo
# from banco.validators.valida_saldo import ValidaSaldo as vs
# from rest_framework import serializers


# class SaldoSerializer(serializers.HyperlinkedModelSerializer):
#     data_credito = serializers.DateTimeField(required=False, default=vs.data_credito)
#     valor_credito = serializers.FloatField(required=False, default=vs.valor_credito)
#     data_debito = serializers.DateTimeField(required=False, default=vs.data_debito)
#     valor_debito = serializers.FloatField(required=False, default=vs.valor_debito)
#     saldo_final = serializers.FloatField(required=False, default=vs.saldo_final)
   
#     class Meta():
#         model = Saldo
#         fields = "__all__"
