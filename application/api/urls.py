from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserProfileViewSet)
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    #rest_framework
    url(r'^', include(router.urls)),
]
