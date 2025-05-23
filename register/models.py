from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(AbstractUser):
#     phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'phone']
#
#     def __str__(self):
#         return self.email or self.phone
#
#     def str(self):
#         return self.email or self.phone
