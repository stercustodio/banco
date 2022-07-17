from banco.models.extrato import Extrato
from banco.serializers import ExtratoSerializer
from rest_framework import permissions, viewsets


class ExtratoViewset(viewsets.ModelViewSet):
    
    serializer_class = ExtratoSerializer
    queryset = Extrato.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    

 