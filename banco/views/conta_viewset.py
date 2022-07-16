from banco.importacoes import Conta, ContaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets


class ContaViewset(viewsets.ModelViewSet):
    
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['cliente', 'numero_conta']
    ordering_fields = ['numero_conta']
