from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Definir permissões se necessário
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['categoria'] 
