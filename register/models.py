<<<<<<< HEAD
=======
from django.db import models

>>>>>>> origin/dan
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

<<<<<<< HEAD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.email or self.phone
=======

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def str(self):
        return self.email or self.phone
>>>>>>> origin/dan
