from rest_framework import serializers
from carts.models import Order, CartItem, Cart
from carts.serializers.nested.cart_items import CartItemsListSerializer


class CartItemsCreateSerializer(serializers.ModelSerializer):
    """Used with create method"""
    class Meta:
        model = CartItem
        fields = (
            'cart',
            'book',
        )
        read_only_fields = ('cart',)


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemsListSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_items',)
        read_only_fields = ('user',)


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    """
    need to fix total_price as well
    """
    class Meta:
        model = Order
        fields = (
            'id',
            'order_date',
            'order_status',
            'total_price',
            'cart',
        )
        read_only_fields = ('cart',)
