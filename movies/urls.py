from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import (Moviesviewset, RandomMovie,
                ScoreMovieViewset, ViewMovieViewset, countviewset, OrderMoviesByparam)

router = DefaultRouter()

router.register(r"api/movies", Moviesviewset, basename="movies")
router.register(r"api/random", RandomMovie, basename="Random")
router.register(r"api/orderbyparam", OrderMoviesByparam, basename="Filter")
router.register(r"api/scoremovie", ScoreMovieViewset, basename="score")
router.register(r"api/viewmovie", ViewMovieViewset, basename="view")
router.register(r"api/mean", countviewset, basename="mean")


urlpatterns = router.urls

