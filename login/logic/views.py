from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from logic.models import Student
from logic.serializer import StudentSerializer

# Create your views here.

# Student

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerStudent(request):
    user = request.user
    request.data ['UserID'] = user.UserID
    if user.is_staff == False:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)
    else:
        content = {
            'msg':'You are not parent hence you can not access this'
        }
        return Response(content)
    
# get all students
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllStudent(request):
    user = request.user
    if user.is_staff == True:
        student = Student.objects.all()
        # STAFF CAN SEE STUDENTS
        if len(student) > 0:
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data, status=200)
        else:
            content = {
                'Greeting' : 'Hi Staff, There is no any student',
                'message' : 'You should consider marketing'
            }
            return Response(content)
    else:
        # PARENT CAN ONLY SEE THEIR STUDENTS
        UserID = request.user.UserID
        student = Student.objects.filter(UserID=UserID)
        if len(student) > 0:
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data, status=200)
        else:
            content = {
                'Greeting':'Hi, You have not registerd any student',
                'message':'Kindly Contact us to assist you with registration'
            }
            return Response(content)