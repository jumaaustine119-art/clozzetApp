from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer,User

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        serializer=User(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




class CategoryView(APIView):
       def get(self,request):
           categories=Category.objects.all()
           serializers=CategorySerializer(categories,many=True)
           return Response(serializers.data)
        
       def post(self,request):
           serializers=CategorySerializer(data=request.data)
           if serializers.is_valid():
               serializers.save()
               return Response(serializers.data)
           return Response(serializers.errors)
            

class ProductView(APIView):
    def get(self,request):
        Products=Product.objects.all()
        serializers=ProductSerializer(Products,many=True)
        return Response(serializers.data)
    

    def post(self,request):
        serializers=ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
            
            