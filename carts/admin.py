from django.contrib import admin
from carts.models import Order, OrderItem


class ProfileAdmin(admin.StackedInline):
    model = OrderItem
    fields = ('order', 'book', 'quantity', 'price_at_order',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'order_date',
                    'order_status', 'total_price',)
    list_display_links = ('order_id', 'user', 'order_date',)
    readonly_fields = ('order_id', 'order_status')
    search_fields = ('user', 'order_date', 'order_id',)
    inlines = (ProfileAdmin,)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'price_at_order',)
    list_display_links = ('order', 'book',)
    readonly_fields = ('order',)

    search_fields = ('order',)
