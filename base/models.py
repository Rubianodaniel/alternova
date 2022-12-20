from django.db import models

# Create your models here.
class BaseModel(models.Model):
    
    # TODO:
    id = models.AutoField(primary_key=True)
    created_date = models.DateField("created date", auto_now=False, auto_now_add= True)
    modify_date = models.DateField("Modify date", auto_now=True, auto_now_add= False)
    deleted_date = models.DateField("Deleted date", auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "Base model"
        