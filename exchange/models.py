from django.db import models

# Create your models here.

class ExchangeProgram(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    places = models.CharField(max_length=50)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name