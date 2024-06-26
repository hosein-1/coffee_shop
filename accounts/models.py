from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    email_confirmed = models.BooleanField(default=False)
