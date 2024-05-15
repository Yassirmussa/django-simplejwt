from rest_framework import serializers

from logic.models import Student
from account.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='UserID', read_only=True)
    class Meta:
        model = Student
        fields = ['StuID','SName','Address','BirthDate','UserID','user']