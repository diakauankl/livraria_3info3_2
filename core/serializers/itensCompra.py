from core.models import Compra, ItensCompra
from core.serializers.categoria import ModelSerializer


class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')
        depth = 1
