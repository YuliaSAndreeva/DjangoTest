from rest_framework import serializers

from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'pk',
            'name',
            'description',
            'price',
            'discount',
            'created_at',
            'archived',
            'author',
        )

    def get_author(self, obj):
        return obj.author.username


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'