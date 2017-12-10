from django.conf.urls import url

from . import views
from .views import ProductListView


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^ajax_list/$', views.ajax_list, name='ajax_list'),
    url(r'^list/$', ProductListView.as_view(), name='list'),
    url(r'^(?P<category_slug>[-\w]+)$',
        views.product_list,
        name='product_listi_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)$', views.product_detail,
        name='product_detail'),
]
