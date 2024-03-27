from django.contrib import admin
from carts.models import Order, CartItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date',
                    'order_status', 'total_price',)
    list_display_links = ('id', 'order_date',)
    readonly_fields = ('id', 'order_status')
    search_fields = ('order_date', 'id',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'book',)
    list_display_links = ('cart', 'book',)
    search_fields = ('cart',)
