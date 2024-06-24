from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/images/%Y/%m/%d/', blank=True, null=True, verbose_name='Фотография')

    def __str__(self):
        return self.username