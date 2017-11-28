import xadmin

from .models import Order, OrderItem


class OrderItemInline(object):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(object):
    list_display = ['id', 'username', 'address', 'postal_code',
                    'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


xadmin.site.register(Order, OrderAdmin)
