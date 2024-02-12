from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self) -> str:
        return self.username
    