from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile=models.CharField(max_length=10)
    pic = models.ImageField( upload_to='pictures/profiels', blank=True)