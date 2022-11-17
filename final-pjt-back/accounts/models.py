from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # password_confirm = models.CharField(max_length=128)
