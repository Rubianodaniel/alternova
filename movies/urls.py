from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import (Moviesviewset, RandomMovie, FilterMovieByName,
                ScoreMovieViewset, ViewMovieViewset, ListMoviesViewset)

router = DefaultRouter()

router.register(r"api/movies", Moviesviewset, basename="movies")
router.register(r"api/random", RandomMovie, basename="Random")
router.register(r"api/filterbyname", FilterMovieByName, basename="Filter")
router.register(r"api/scoremovie", ScoreMovieViewset, basename="score")
router.register(r"api/viewmovie", ViewMovieViewset, basename="view"),
router.register(r"api/listmovies", ListMoviesViewset, basename="listmovie")

urlpatterns = router.urls

