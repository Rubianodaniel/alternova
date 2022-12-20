import random

from rest_framework import viewsets, permissions
from rest_framework.response import Response  
from rest_framework.views import APIView

from .models import Movies, ScoreMovie
from .serializers import MoviesSerializer

class Moviesviewset(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Movies.objects.all().order_by("name").values()


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
            "views":data.views,
            "mean_score":data.mean_score
        } 

        return Response(data)


class FilterMovieByName(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Movies.objects.all()
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(name=self.kwargs["name"])
    

        
        









