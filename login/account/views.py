from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes

from account.serializers import CustomTokenObtainPairSerializer, UserSerializer
from account.models import User

# Create your views here.

# Custom Login
@api_view(['POST'])
def login(request):

    serializer = CustomTokenObtainPairSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.user
    tokens = serializer.validated_data
    # Get additional user information

    if user.is_staff == True and user.is_superuser == True:

        user_info = {
            'userID': user.UserID,
            'firstname': user.first_name,
            'role':'staff',
            'admin':'admin'
        }
        # Add user information to the response data
        response_data = {
            'refresh': tokens['refresh'],
            'access': tokens['access'],
            'user_info':user_info
        }
        return Response(response_data, status=200)
    elif user.is_staff == True:
        user_info = {
            'userID': user.UserID,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'role':'staff'
        }
        
        response_data = {
            'refresh': tokens['refresh'],
            'access': tokens['access'],
            'user_info':user_info
        }
        return Response(response_data, status=200)
    else:
        user_info = {
            'userID': user.UserID,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'role':'parent'
        }
        
        response_data = {
            'refresh': tokens['refresh'],
            'access': tokens['access'],
            'user_info':user_info
        }
        return Response(response_data, status=200)



    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tryAuthenticate(request):
    user = request.user
    if user.is_staff == True:
        content = {
                'email':user.email,
                'status':'Staff'
            }
        return Response(content)
    else:
        content = {
            'email':user.email,
            'status':'Parent'
        }
        return Response(content)

@api_view(['POST'])
def insertUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  
    return Response(serializer.errors, status=400) 


@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=200)


@api_view(['PUT'])
def updateUser(request, UserID):
    try:
        user = User.objects.get(UserID = UserID)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f"User with ID {UserID} does not exist")

@api_view(['DELETE'])
def deleteUser(request, UserID):
    try:
        user = User.objects.get(UserID = UserID)
        user.delete()
        return Response(f"User with ID {UserID} deleted successifully")
    except:
        return Response(f"User with ID {UserID} does not exist")

@api_view(['DELETE'])
def deleteAllUser(request):
    user = User.objects.all()
    user.delete()
    return Response("All user deleted successifully")

