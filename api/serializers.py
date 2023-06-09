from rest_framework import serializers
from .models import Promocao, Empresa, Loja

"""serializers.HyperlinkedModelSerializer para trabalhar com relacionamentos"""
class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = ['id', 'nome']

class LojaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loja
        fields = ['id', 'nome', 'endereco', 'empresa']

class PromocaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promocao
        fields = ['id', 'nome', 'loja']

# class LojaSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Loja
#         fields = ['id', 'nome', 'empresa']
    
#     def add(self, instance):
#         response = super().add(instance)
#         response ['empresa'] = EmpresaSerializer(instance.empresa).data
#         return response

"""
class PromocaoSerializer(serializers.ModelSerializer):

    
    empresa = serializers.CharField(source='empresa.nome')
    loja = serializers.CharField(source='loja.nome')

    class Meta:
        model = Promocao
        fields = ['id', 'nome', 'empresa', 'loja']
"""