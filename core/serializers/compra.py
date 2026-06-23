from rest_framework.serializers import ModelSerializer

from core.models import compra


class CompraSerializer(ModelSerializer):
    class Meta:
        model = compra
        fields = '__all__'