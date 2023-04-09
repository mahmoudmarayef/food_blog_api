from rest_framework import serializers
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate
from .models import Category, Recipe

# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'first_name', 'last_name']

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#         )
#         return user
    
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     password = serializers.CharField(max_length=128, write_only=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', 'ingredients', 'image', 'category')