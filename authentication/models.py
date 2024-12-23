from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_id = models.CharField(max_length=5,primary_key=True)
    mobile = models.CharField(max_length=13)
    username = None


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class LoginModel(models.Model):
    email = models.TextField()
    password = models.TextField()

