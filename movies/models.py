from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    views = models.IntegerField()
    score = models.IntegerField()
    watched = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
