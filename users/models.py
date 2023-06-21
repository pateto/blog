from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    # set email as username for login
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []
