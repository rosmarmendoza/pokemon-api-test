import requests
import pprint as pp
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Pokemon API  for get Evolution Chain by Input Number of Pokemon'

    def add_arguments(self, parser):
        # Evolution Chain
        parser.add_argument(
            'evolution_chain',
            type=int,
            help='Evolution Chain'
        )

    def handle(self, *args, **options):
        evolution_chain = options.get('evolution_chain')
        evolution_url = f"https://pokeapi.co/api/v2/evolution-chain/{evolution_chain}"
        evolution_response = requests.get(evolution_url)
        if evolution_response.status_code == 200:
            raw_evolution_chain_data = evolution_response.json()
            chain = raw_evolution_chain_data['chain']
            evolves_to = chain['evolves_to']
            pokemon_name = chain['species']['name']
        else:
            print('Error data not found')

            # url api pokemon
        pokemon_detail = options.get('pokemon_detail')
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        pokemon_response = requests.get(pokemon_url)
        if pokemon_response.status_code == 200:
            raw_pokemon_data = pokemon_response.json()
            id = raw_pokemon_data['id']
            name = raw_pokemon_data['name']
            base_stats = raw_pokemon_data['stats']
            height = raw_pokemon_data['height']
            weight = raw_pokemon_data['weight']
            print(id,name,height,weight,base_stats)

