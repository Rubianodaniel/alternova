from rest_framework import serializers
from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("id", "name", "gender", "type", "views", "score", "date_created")
        read_only = ("date_created",) 