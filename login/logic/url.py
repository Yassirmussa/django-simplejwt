from django.urls import path
from logic import views 

urlpatterns = [
    path('registerstudent', views.registerStudent),
    path('getallstudent', views.getAllStudent),
]