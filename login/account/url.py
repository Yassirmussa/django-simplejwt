from account import views
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account.serializers import CustomTokenObtainPairSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

urlpatterns = [
    # path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # custom login hii inatoka kwenye class nloicoment apo juu
    # path('api/token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/token', views.login),

    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('tryAuthenticate', views.tryAuthenticate),

    path('register', views.insertUser),
    path('getusers', views.getUser),
    path('updateuser/<int:UserID>/', views.updateUser),
    path('deleteuser/<int:UserID>/', views.deleteUser),
    path('deleteallusr', views.deleteAllUser),

]