import random
from django.db.models import Count
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response  


from .models import (Movies, ScoreMovie, ViewMovie)
from .serializers import (MoviesSerializer,ListMoviesSerializer, ScoreSerializer,
                        ViewSerializer)


class Moviesviewset(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        data = Movies.objects.all().values()
        
        return data


class ListMoviesViewset(viewsets.GenericViewSet):
    serializer_class = ListMoviesSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        data = Movies.objects.all()
        return data

    def list(self, request):
        data = self.get_queryset()
       
        data = {
            
        } 

        return Response(data)


class RandomMovie(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Movies.objects.all()
    
    def list(self, request):
        data = self.get_queryset()
        data = random.choice(data)
        data = {
            "name":data.name,
            "gender":data.gender,
            "type":data.type,
        } 

        return Response(data)


class FilterMovieByName(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Movies.objects.all()
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(name=self.kwargs["name"])
    

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

  

        









