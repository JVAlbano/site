from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    imagem = models.ImageField(null=True, blank=True, upload_to='usuario')
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

