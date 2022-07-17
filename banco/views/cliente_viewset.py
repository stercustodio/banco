from banco.models.cliente import Cliente
from banco.serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets


class ClienteViewset(viewsets.ModelViewSet):
    
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['nome', 'cpf', 'dt_nascimento']
    ordering_fields = ['nome']
