from django.urls import path
from carts.views import CartAPIView, CreateCartItemAPIView, OrderAPIView

urlpatterns = [
    # orders
    path('orders/', OrderAPIView.as_view(), name='orders'),
    # carts
    path('cart/', CartAPIView.as_view(), name='cart'),
    path('cart/item-create/', CreateCartItemAPIView.as_view(),
         name='cart_item')
]
