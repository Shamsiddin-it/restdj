from django.db import models
from django.urls import reverse

# Create your models here.

class order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    addres = models.CharField(max_length=255)

    def __str__(self):
        return self.name, self.email, self.addres