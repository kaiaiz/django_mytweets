"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from dashing.utils import router

from .widgets import CustomWidget

router.register(CustomWidget, 'custom_widget', eg_kwargs_param="[A-Za-z0-9_-]+")

import xadmin
from xadmin.plugins import xversion
xversion.register_models()
xadmin.autodiscover()


urlpatterns = [
#    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^shop/', include('shop.urls', namespace="shop")),
    url(r'^summernote/', include('django_summernote.urls',)),
    url(r'^dashboard/', include(router.urls, namespace="Dashboard")),
#    url(r'^search/', include('haystack.urls', namespace="haystack")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
