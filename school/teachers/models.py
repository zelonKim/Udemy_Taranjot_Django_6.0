from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    bio = models.TextField()