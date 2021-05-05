from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from pokemon.viewsets import PokemonViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'pokemons', PokemonViewSet, basename="pokemons")

urlpatterns = [
    path('', include(router.urls)),
]
