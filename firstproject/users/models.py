from django.db import models
from django.contrib.auth.models import User
from django.utils.tree import Node

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
