from django.urls import path
from .views import CategoryView, RecipeView #UserRegistrationView, LoginView, 

urlpatterns = [
    #path('register/', UserRegistrationView.as_view(), name='user-registration'),
    #path('login/', LoginView.as_view(), name='login'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('recipes/', RecipeView.as_view(), name='recipes'),
]