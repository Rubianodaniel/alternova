from django.db import models
from base.models import BaseModel

class Movies(BaseModel):
    
    # TODO;
    name = models.CharField("name", max_length=100, blank = False, null=False, unique = True)
    gender = models.CharField("gender", max_length=50 , blank=False , null= False)
    type = models.CharField("type", max_length=20, blank=False , null = False)
    
    class Meta:
        verbose_name = "Movies"

class ScoreMovie(BaseModel):

    # TODO:
    score = models.IntegerField()
    name_id  = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name= "Movie Name")

    class Meta:
        verbose_name= "score"
        
    def __str__(self) -> str:
        return self.score
    


class ViewMovie(BaseModel):

    # TODO:
    view = models.BooleanField(default=False)
    name_id  = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name= "Movie Name")

    class Meta:
        verbose_name= "Views"

   



