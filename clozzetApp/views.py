from django.shortcuts import render
from .models import Category, Product
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer, ProductSerializer, UserRegistrationSerializer, UserLoginSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
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
            


class SingleProductView(APIView):
    def get(self, request,id):
        products = get_object_or_404(Product,id=id)
        serializers=ProductSerializer(products)
        return Response(serializers.data)

    def put(self,request,id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        products = get_object_or_404(Product,id=id)
        products.delete()
        return Response({"messege":"product was deleted"})
        


class UseLoginView(APIView):
    def post(self,requst):
        serializer = UserLoginSerializer(data=requst.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token
                return Response({'access_token': str(access),
                                 'refresh_token': str(refresh),
                                 'userData':{
                                     'name':user.name,
                                     'is_admin':user.is_staff
                                 }
                                 })
            return Response({'message': 'invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)






         
              