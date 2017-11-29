import xadmin

from .models import Coupon


class CouponAdmin(object):
    list_display = ['code', 'valid_from', 'valid_to',
                    'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']


xadmin.site.register(Coupon, CouponAdmin)
