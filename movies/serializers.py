from rest_framework import serializers
from .models import Movies,ScoreMovie

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        exclude = ('created_date','modify_date','deleted_date')
    
  

      

class ScoreSerializer(serializers.ModelSerializer):
    class meta:
        model = ScoreMovie
        exclude = ('created_date','modify_date','deleted_date')