from django.db import models


class Login(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()

    def __str__(self):
        return self.Email
# Create your models here.
