import random
from django.db.models import Count, Avg
from rest_framework import status,filters
from rest_framework import viewsets, permissions
from rest_framework.response import Response  


from .models import (Movies, ScoreMovie, ViewMovie)
from .serializers import (MoviesSerializer, ScoreSerializer,ViewSerializer)


class Moviesviewset(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer 
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","gender", "type")

    
    def get_queryset(self):
        data = Movies.objects.all()
        return data


class RandomMovie(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Movies.objects.all()
    
    def list(self, request):
        data = self.get_queryset()
        data = random.choice(data)
        print(data.mean_score)
        data = {
            "name":data.name,
            "gender":data.gender,
            "type":data.type,     
        } 

        return Response(data)



class ScoreMovieViewset(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ScoreMovie.objects.all()


class ViewMovieViewset(viewsets.ModelViewSet):
    serializer_class = ViewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ViewMovie.objects.all()





    

  

        









