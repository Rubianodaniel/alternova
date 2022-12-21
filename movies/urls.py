from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import (Moviesviewset, RandomMovie, FilterMovieByName,
                ViewMovie)

router = DefaultRouter()

router.register(r"api/movies", Moviesviewset, basename="movies")
router.register(r"api/random", RandomMovie, basename="Random")
router.register(r"api/filter", FilterMovieByName, basename="Filter")
router.register(r"api/scoreMovie", ViewMovie, basename="score")

urlpatterns = router.urls

