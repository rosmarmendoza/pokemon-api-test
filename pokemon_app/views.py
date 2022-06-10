from django.shortcuts import get_object_or_404
from pokemon_app.models import PokemonModel
from django.http import HttpResponse
from django.core import serializers


def search(request, name):
    pokemon = get_object_or_404(PokemonModel, pokemon_name=name)
    serialized_pokemon = serializers.serialize('json', [pokemon, ])
    return HttpResponse(serialized_pokemon)

