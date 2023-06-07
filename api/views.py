from django.shortcuts import render

from django.http import JsonResponse
# from .models import Promocao, Empresa, Loja
from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = (AllowAny,)

"""
class UserProgramViewset(viewsets.ModelViewSet):
     permission_classes = [
        permissions.IsAuthenticated
     ]
     serializer_class = UserProgramSerializers
     
     def get_queryset(self):
        return UserProgram.objects.filter(user=self.request.user)    

     def perform_create(self, serializer):
        serializer.save(user=self.request.user)
"""

"""
@api_view(['GET', 'POST'])
def promocao_list(request, format=None):
    if request.method == 'GET':
        promocao = Promocao.objects.all()
        serializer = PromocaoSerializer(promocao, many=True)
        return JsonResponse({'promocoes': serializer.data})
 
    if request.method == 'POST':
        serializer = PromocaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        
@api_view(['GET', 'PUT', 'DELETE'])
def promocao_detail(request, id, format=None):
    
    try:
        promocao = Promocao.objects.get(pk=id)
    except Promocao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PromocaoSerializer(promocao)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PromocaoSerializer(promocao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        promocao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""