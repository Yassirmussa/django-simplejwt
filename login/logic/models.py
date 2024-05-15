from django.db import models
from  account.models import User
# Create your models here.

class Student(models.Model):
    StuID = models.AutoField(primary_key=True)
   

    SName = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)
    BirthDate = models.DateField()
    
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'student'