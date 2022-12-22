from rest_framework import serializers
from .models import Movies,ScoreMovie, ViewMovie


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        exclude = ('created_date','modify_date','deleted_date')

    def validate_type(self, value):
        if value == "serie" or value == "movie":
            return value
        raise serializers.ValidationError("Error type must be serie or movie")


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
            "name":instance.name_id.name
        }
        return data



class ViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewMovie
        exclude = ('created_date','modify_date','deleted_date')

    def to_representation(self, instance):
        data = {
            "view": instance.view,
            "name": instance.name_id.name
        }
        return data


class ListMoviesSerializer(serializers.ModelSerializer):
    score = serializers.StringRelatedField()

    class Meta:
        model = Movies()
        exclude = ('created_date','modify_date','deleted_date')

    