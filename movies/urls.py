from rest_framework import routers
from .api import Moviesviewset

router = routers.DefaultRouter()

router.register("api/movies", Moviesviewset, "movies")

urlpatterns =  router.urls