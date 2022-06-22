from rest_framework import serializers
from product.models import Product as ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['user', 'title', 'thumbnail', 'contents', 'posting_date',
                  'expire_date', 'cost', 'updated_at', 'is_active', ]

                  
