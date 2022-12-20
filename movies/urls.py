from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import Moviesviewset
#from .api import movies_view

router = DefaultRouter()

router.register(r"api/movies", Moviesviewset, basename="movies")

urlpatterns = router.urls

# urlpatterns =  [
    # path("api/movies/", movies_view, name= "movies")
# ]