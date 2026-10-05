from django.db import models

# Create your models here.

class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200)
    name = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    languages = models.CharField(max_length=200)
    places = models.CharField(max_length=50)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university