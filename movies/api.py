from .models import Movies
from rest_framework.response import Response  
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
#from rest_framework.decorators import api_view
from .serializers import MoviesSerializer

class Moviesviewset(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MoviesSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state=True).first()
         





""" @api_view(["GET","POST"])
def movies_view(request):
    if request.method == "GET":
        movie = Movies.objects.all()
        movie_serializer = MoviesSerializer(movie, many=True)
        return Response(movie_serializer.data)
    
    elif request.method == "POST":
        movie_serializer = MoviesSerializer(data = request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        else:
            Response(movie_serializer.errors) """