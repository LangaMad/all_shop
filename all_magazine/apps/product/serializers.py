from rest_framework import serializers
from .models import *


class TestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestProduct
        fields = '__all__'















