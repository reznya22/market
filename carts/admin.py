from django.contrib import admin
from carts.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'order_date', 'order_status', 'total_price',)
    list_display_links = ('order_id', 'user', 'order_date',)


    search_fields = ('user', 'order_date', 'order_id',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'price_at_order',)
    list_display_links = ('order', 'book',)

    search_fields = ('order',)
