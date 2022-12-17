from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    views = models.IntegerField()
    score = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
