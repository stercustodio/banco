# from rascunho.saldo import Saldo
# from banco.serializers import SaldoSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters, permissions, viewsets


# class SaldoViewset(viewsets.ModelViewSet):
    
#     serializer_class = SaldoSerializer
#     queryset = Saldo.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     filter_backends = [
#         DjangoFilterBackend,
#         filters.OrderingFilter,
#         filters.SearchFilter
#     ]
#     search_fields = [
#         'conta_consultada',
#         'entradas',
#         'saidas',
#         'saldofinal'
#     ]
#     ordering_fields = ['conta_consultada']
