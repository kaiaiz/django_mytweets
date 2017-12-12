from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib import admin

from dashing.utils import router

from .widgets import CustomWidget
#from application.about.models import UserProfile

router.register(CustomWidget, 'custom_widget', eg_kwargs_param="[A-Za-z0-9_-]+")

import xadmin
from xadmin.plugins import xversion
xversion.register_models()
xadmin.autodiscover()


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^cart/', include('cart.urls', namespace="cart")),
    url(r'^orders/', include('orders.urls', namespace="orders")),
    url(r'^shop/', include('shop.urls', namespace="shop")),
    url(r'^coupons/', include('coupons.urls', namespace="coupons")),
    url(r'^summernote/', include('django_summernote.urls',)),
    url(r'^dashboard/', include(router.urls, namespace="Dashboard")),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^notifications/', include('notifications.urls', namespace="notifications")),
#    url(r'^search/', include('haystack.urls', namespace="haystack")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
