from rest_framework import serializers
from .models import Promocao

class PromocaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promocao
        fields = ['id', 'empresa', 'loja', 'promocao']