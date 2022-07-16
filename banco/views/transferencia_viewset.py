from banco.importacoes import Transferencia, TransferenciaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets


class TransferenciaViewset(viewsets.ModelViewSet):
    
    serializer_class = TransferenciaSerializer
    queryset = Transferencia.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = [
        'conta_origem',
        'conta_destino',
        'valor_transferencia',
        'data_transferencia'
        ]
    ordering_fields = ['data_transferencia']
