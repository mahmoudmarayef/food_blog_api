#from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, RecipeSerializer #RegistrationSerializer, LoginSerializer
#from rest_framework_simplejwt.tokens import RefreshToken
#from django.contrib.auth import authenticate, login
from .models import Category, Recipe

# class UserRegistrationView(generics.CreateAPIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token = RefreshToken.for_user(user)
#             return Response({
#                 'token': str(token.access_token),
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     'access': str(refresh.access_token),
#                     'refresh': str(refresh),
#                 })
#             else:
#                 return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class RecipeView(APIView):
    def get(self, request):
        category = request.query_params.get('category', None)
        if category:
            recipes = Recipe.objects.filter(category=category)
        else:
            recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)