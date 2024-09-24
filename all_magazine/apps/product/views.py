from django.shortcuts import render
from rest_framework import generics,views,viewsets,response
from .serializers import *
from apps.product.models import TestProduct
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from .custom_api_view import *
from .serializers import *
from rest_framework.viewsets import GenericViewSet
from .custom_permissions import *

class TestProductViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = TestProduct.objects.all()
    serializer_class = TestProductSerializer
    permission_classes = (IsAuthenticated,)

# class CarViewSet(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.ListModelMixin,
#                     GenericViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = (IsAdminOrReadOnly,)


class TestProductApiView(viewsets.ViewSet):
    serializer_class = TestProductSerializer

    def list(self, request):
        queryset = TestProduct.objects.all()
        serializer = TestProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TestProduct.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TestProductSerializer(user)
        return Response(serializer.data)






# class  TestProductListApiView(generics.ListAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = TestProductSerializer
#
#
# class TestProductCreateApiView(generics.CreateAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = TestProductSerializer
#
# class TestProductRetrieveApiView(generics.RetrieveAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = TestProductSerializer
#
class CarListCreateApiView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
#
# class TestProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = TestProductSerializer
#
# class TestProductRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = TestProductSerializer
#
class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# class TestProductApiView(views.APIView):
#     def get(self,request):
#         return response.Response({'message':'Hello World'})
#
#     def post(self, requset):
#         return response.Response({'message':'Hello Post'})

# api metods

# GET - метод для получения данных
# HEAD - метод для получения заголовков ответа
# OPTIONS - метод для получения доступных методов

# POST - метод для отправки данных
# PUT - метод для обновления данных
# DELETE - метод для удаления данных
# PATCH - метод для частичного обновления данных