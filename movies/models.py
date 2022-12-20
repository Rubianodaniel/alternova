from django.db import models
from base.models import BaseModel


class Movies(BaseModel):
    
    # TODO;
    name = models.CharField("name", max_length=100, blank = False, null=False, unique = True)
    gender = models.CharField("gender", max_length=50 , blank=False , null= False)
    type = models.CharField("type", max_length=20, blank=False , null = False)
    views = models.IntegerField(blank=True, null=True)
    mean_score = models.DecimalField(decimal_places=2,max_digits=4, blank=True, null=True)

    class Meta:
        verbose_name = "Movies"


    def __str__(self) -> str:
        return self.name

class ScoreMovie(BaseModel):

    # TODO:
    score = models.IntegerField()
    name  = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name= "Movie Name")

    class Meta:
        verbose_name= "score"


class ViewMovie(BaseModel):

    # TODO:
    View = models.BooleanField(default=False)
    name  = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name= "Movie Name")

    class Meta:
        verbose_name= "Views"

    def __str__(self) -> str:
        return self.name
