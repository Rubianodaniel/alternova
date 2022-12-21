import random
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response  
from rest_framework.views import APIView

from .models import Movies, ScoreMovie
from .serializers import MoviesSerializer, ScoreSerializer

class Moviesviewset(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Movies.objects.all().order_by("name").values()
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs["pk"])

    def update(self, request , pk = None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object.get(), data = request.data)
            print(serializer)
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Indicador actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)   



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
    


class ViewMovie(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ScoreMovie.objects.all()

        









