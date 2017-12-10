from django.shortcuts import render
from django.http import Http404

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from shop.models import Product
from about.models import UserProfile
from .serializers import UserProfileSerializer
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classess = (JSONRenderer,)
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
