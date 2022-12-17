from .models import Movies
from rest_framework import viewsets, permissions
from .serializers import MoviesSerializer

class Moviesviewset(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MoviesSerializer