from rest_framework import serializers

from shop.models import Product
from about.models import UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'is_staff')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'slug', 'image',
                  'description', 'price', 'stock', 'available')




