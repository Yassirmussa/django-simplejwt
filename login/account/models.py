from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class User(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Phone_number = models.CharField(max_length=10)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="user_groups",
        related_query_name="users",
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="user_permissions",
        related_query_name="users",
    )

    class Meta:
        db_table = 'users'
