from rest_framework import serializers
from .models import Category, Product, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        # include the correct phone field name (phone_number)
        fields = ['id', 'name', 'email', 'password', 'phone_number', 'address']

    def create(self, validated_data):
        # pop password so it's not passed twice
        password = validated_data.pop('password')
        # Use get with defaults to avoid KeyError if fields are missing
        user = User.objects.create_user(
            email=validated_data.get('email'),
            password=password,
            name=validated_data.get('name'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address', ''),
        )
        return user




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','description','price','image','created_at','category']



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()