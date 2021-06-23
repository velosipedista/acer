from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    # hobby = models.CharField(max_length=30)
