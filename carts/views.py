from rest_framework import generics
from carts.models import Order, Cart
from rest_framework.permissions import IsAuthenticated
from carts.serializers.api.carts import (
    CartItemsCreateSerializer,
    OrderSerializer,
    CartSerializer
)
from common.permissions import IsAuthorOnly


class OrderAPIView(generics.ListCreateAPIView):
    """Get or create an order/(list of orders)"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(cart__user=self.request.user)
        return queryset

    # if user have a cart, order will be created
    def create(self, request, *args, **kwargs):
        """
        Need to add error handler if user doesn't have a cart
        """
        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            self.kwargs['cart'] = cart
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(cart=self.kwargs['cart'])


class CartAPIView(generics.ListAPIView):
    """Getting the user cart(we need no pk because it's ListAPIView,
    but user could have only one cart)"""
    permission_classes = [IsAuthorOnly]

    def get_serializer_class(self):
        return CartSerializer

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user)
        return queryset


class CreateCartItemAPIView(generics.CreateAPIView):
    """Create items for user cart"""
    serializer_class = CartItemsCreateSerializer
    permission_classes = [IsAuthenticated]

    # if user doesn't have a cart, cart will be created
    def create(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=self.request.user).first()
        if not cart:
            cart = Cart.objects.create(user=self.request.user)
        self.kwargs['cart'] = cart
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(cart=self.kwargs['cart'])
