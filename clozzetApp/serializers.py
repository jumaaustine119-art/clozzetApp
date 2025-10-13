from rest_framework import serializers
from .models import Category, Product,User

class UserRedistrationSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)
    
    class Mata:
        model=User
        fields=['id','name','email','password','password_number','address']

    def create(self,validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
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

