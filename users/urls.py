from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
     path('register/', RegisterView.as_view(), name='register'),# колдонуучу катталуучу URL (жаны аккаунт тузу учун)
    path('login/', LoginView.as_view(), name='login'),#колдонуучу системага кирүү үчүн URL
]
