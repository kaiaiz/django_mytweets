import xadmin

from .models import Category, Product


class CategoryAdmin(object):
    list_display = ['name', 'slug']
    list_filter = ('name',)


class ProductAdmin(object):
    list_display = ['category', 'name', 'slug', 'image', 'description',
                    'price', 'stock', 'available', 'created', 'updated']
    list_display = ('category', 'name')


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Product, ProductAdmin)
