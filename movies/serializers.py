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
    


class MoviesSerializer(serializers.ModelSerializer):
       
    class Meta: 
        model = Movies
        fields = (
            "id", "name", "gender","type", "mean_score", "views"
        )
        read_only_fields = ("id", "mean_score", "views")


    def validate_type(self, value):
        if value == "serie" or value == "movie":
            return value
        raise serializers.ValidationError("Error type must be serie or movie")

    
    def to_representation(self, instance):
    
        query_mean_score = ScoreMovie.objects.values("name").annotate(Avg("score")).order_by()
        mean_score = []
        for element in query_mean_score:
            if element["name"] == instance["id"]:
                mean_score.append(element["score__avg"])

        query_count_views = ViewMovie.objects.values("name").filter(view = 1).annotate(Count("name")).order_by()
        count_views = []
        for element in query_count_views:
            if element["name"]== instance["id"]:
                count_views.append(element["name__count"])

        
        data ={
            "id": instance["id"],
            "name":instance["name"],    
            "gender": instance["gender"], 
            "mean_score": mean_score[0] if len(mean_score) != 0 else "null",
            "views" : count_views[0] if len(count_views) != 0 else "null"
        }
        return data

        
