from django.shortcuts import render
from rest_framework import generics,views,viewsets,response
from .serializers import *
# Create your views here.

class TestProductApiView(generics.ListAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = TestProductSerializer




# class TestProductApiView(views.APIView):
#     def get(self,request):
#         return response.Response({'message':'Hello World'})
#
#     def post(self, request):
#         return response.Response({'message':'Hello World from post'})





# Методы api

# GET - метод для получения данных
# POST - метод для отправки данных
# PUT - метод для обновления данных
# DELETE - метод для удаления данных
# PATCH - метод для частичного обновления данных
# HEAD - метод для получения заголовков ответа
# OPTIONS - метод для получения доступных методов





