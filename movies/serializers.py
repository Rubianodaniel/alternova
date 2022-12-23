from django.db.models import Count, Avg
from rest_framework import serializers
from .models import Movies,ScoreMovie, ViewMovie, MeanScoreMovie


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreMovie
        exclude = ('created_date','modify_date','deleted_date')

    def validate_score(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("Error score must be between 0 and 5")
        return value

    def to_representation(self, instance):
       
        data = {
            "score":instance.score,
            "name":instance.name.name
        }
        return data

        

class MeanScoreSerializer(serializers.Serializer):
    data = ScoreMovie.objects.values("name").annotate(Avg("score")).order_by()
    
    # class Meta:
    #     model = ScoreMovie
    #     exclude = ()

    # def to_representation(self, instance):
    #     data = {
    #         "name":instance["name"],
    #         "score": instance["score__avg"]
    #     }
    #     return data
   


class ViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewMovie
        exclude = ('created_date','modify_date','deleted_date')

    def to_representation(self, instance):
        data = {
            "view": instance.view,
            "name": instance.name.name
        }
        return data
    

class CountViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewMovie
        exclude = ('created_date','modify_date','deleted_date')

    def to_representation(self, instance):
        data = {
            "view": instance["name"],
            "name": instance["name__count"]
        }
        return data




class MoviesSerializer(serializers.ModelSerializer):

    
                

    class Meta: 
        model = Movies
        fields = (
            "id", "name", "gender","type", "mean_score"
        )
        read_only_fields = ("id", "mean_score")


    def validate_type(self, value):
        if value == "serie" or value == "movie":
            return value
        raise serializers.ValidationError("Error type must be serie or movie")

    
    def to_representation(self, instance):
        '''select avg(movies_scoremovie.score), movies_movies.name
            from movies_scoremovie
            INNER JOIN movies_movies ON movies_scoremovie.name_id = movies_movies.id
            GROUP BY name'''
        
        data ={
            "name":instance["name"],    
            "gender": instance["gender"],
            #"mean_score": mean_score
        }
        return data

        
