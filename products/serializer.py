from rest_framework import serializers
from .models import ProductModel
class ProductSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(read_only=true)
    
    class Meta:
        model = ProductModel
        fields = '__all__'