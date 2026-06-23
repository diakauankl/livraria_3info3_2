from rest_framework.serializers import CharField, ModelSerializer

from core.models import compra


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    class Meta:
        model = compra
        fields = '__all__'