import random
from django.db.models import Count, Avg
from rest_framework import status,filters
from rest_framework import viewsets, permissions
from rest_framework.response import Response  


from .models import (Movies, ScoreMovie, ViewMovie)
from .serializers import (MoviesSerializer, ScoreSerializer,MeanScoreSerializer,
                        ViewSerializer, CountViewSerializer)


class Moviesviewset(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer 
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","gender", "type")

    
    def get_queryset(self):
        data = Movies.objects.all().values()
        mean_score = Movies.objects.select_related("name_id")
        print(mean_score.query)
        return data






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


class OrderMoviesByparam(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    
    def get_queryset(self, request):
        return Movies.objects.all()
    
    def get_object(self, value="name"):
        return self.get_serializer().Meta.model.objects.filter(name=self.kwargs[value])
    

class ScoreMovieViewset(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ScoreMovie.objects.all()


class MeanViewset(viewsets.GenericViewSet):

    # serializer_class = MeanScoreSerializer
    # permission_classes = [permissions.AllowAny]
    
    # def get_queryset(self):
    #     data = ScoreMovie.objects.values("name").annotate(Avg("score")).order_by()
    #     return data
      
    # def list(self, request):
    #     data = self.get_queryset()
    #     return Response(data)
    pass


class ViewMovieViewset(viewsets.ModelViewSet):
    serializer_class = ViewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ViewMovie.objects.all()



class CountViewsViewset(viewsets.GenericViewSet):
    serializer_class = CountViewSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        data = ViewMovie.objects.values("name").filter(view = 1).annotate(Count("name")).order_by()
        return data 

    def list(self, request):
        data = self.get_queryset()
        return Response(data)
        

    

  

        









