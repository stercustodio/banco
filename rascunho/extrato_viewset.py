# import django_filters
# from banco.importacoes import Saldo


# class ExtratoViewset(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='pk')
    
#     class Meta:
#         model = Saldo
#         fields = ['numero_conta', 'saldo_data', 'saldo_valor']

#     def get_routes(self, ExtratoViewset):
#         extra_actions = viewset.get_extra_actions()
#         detail_actions = [action for action in extra_actions if action.detail]
#         list_actions = [action for action in extra_actions if not action.detail]
    
#     def historico_movimentacao(numero_conta):
#         valores = []
#         datas = []
        
#         if numero_conta == Transferencia.conta_destino:
#             valor = Transferencia.valor_transferencia
#             valores.append(valor)
#             datas.append(Transferencia.data_transferencia)
#         elif numero_conta == Transferencia.conta_origem:
#             valor = (-1)*Transferencia.valor_transferencia
#             valores.append(valor)        
#             datas.append(Transferencia.data_transferencia)
            
#         movimentacao = dict(key=datas, values=valores)
            
#         return movimentacao        
    