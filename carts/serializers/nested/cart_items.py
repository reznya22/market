from rest_framework import serializers
from carts.models import CartItem


class CartItemsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('book',)
