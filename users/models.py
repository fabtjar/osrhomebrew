from django.contrib.auth.models import AbstractUser
from django.db import models

from monsters.models import Monster


class CustomUser(AbstractUser):
    liked_monsters = models.ManyToManyField(Monster)
