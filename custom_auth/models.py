from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    age = models.PositiveIntegerField(null=True, blank=True)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.username
