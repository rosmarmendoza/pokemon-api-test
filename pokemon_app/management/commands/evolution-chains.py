from pokemon_app.services import poke_api_services
from django.core.management.base import BaseCommand
from pokemon_app.models import PokemonModel
import pprint as pp


class Command(BaseCommand):
    help = 'Pokemon API  for get Evolution Chain by Input Number of Pokemon'

    def add_arguments(self, parser):
        # Evolution Chain
        parser.add_argument(
            'evolution_chain_id',
            type=int,
            help='Evolution Chain Id'
        )

    def handle(self, *args, **options):
        # Get Chain Pokemon
        chain_id = options.get('evolution_chain_id')
        # import pdb; pdb.set_trace()
        if chain_id > 0:
            service_api = poke_api_services.PokeApiService()
            data_evolution_chain = service_api.chain_evolution(
                evolution_chain_id=chain_id)

            pokemon_list = self.management_chain_evolution(
                data_evolution_chain=data_evolution_chain,
                service_api=service_api)
            # TODO Guardar la lista de pokemones en la Base de Datos SQLite

            saved_datastore = \
                self.datastore_list_pokemon(pokemon_list=pokemon_list)
            print(f"For this evolution chain id {chain_id},"
                  f" the pokemon list is: ",
                  pokemon_list)
            # complementar con la variable de saved_datastored
        else:
            raise Exception("Evolution Chain Id must be major to 0")

    def management_chain_evolution(self, data_evolution_chain, service_api):
        # management data with keys this function treatment the dict
        chain = data_evolution_chain['chain']

        if chain:
            # case 1 (n) bulbasur
            pokemon_list = []
            # pokemon_name
            pokemon_name = chain['species']['name']
            data_pokemon = service_api.pokemon_info(pokemon_name=pokemon_name)
            pokemon_info = self.management_pokemon(data_pokemon=data_pokemon)
            evolves_to = chain['evolves_to']
            evolutions_info = self.search_evolutions(evolves_to=evolves_to)
            pokemon_info['evolutions'] = evolutions_info
            # length = len(pokemon_info) + 1
            pokemon_list.append(pokemon_info)


            # TODO case 2 (n+1) bulbasur -> evolves_to
            '''for i in length:
                pokemon_list[i].append(pokemon_info)
            '''
            return pokemon_list
        else:
            raise Exception("Chain not was found")

    def management_pokemon(self, data_pokemon):
        pokemon_information = {}
        pokemon_information['id'] = data_pokemon['id']
        pokemon_information['name'] = data_pokemon['name']
        pokemon_information['height'] = data_pokemon['height']
        pokemon_information['weight'] = data_pokemon['weight']

        length = len(data_pokemon['stats'])
        pokemon_information['base_stats'] = []
        for i in range(length):
            pokemon_information['base_stats'].append(
                data_pokemon['stats'][i]['base_stat'])
        return pokemon_information

    def search_evolutions(self, evolves_to):
        evolutions = []
        # print("Evolution>>", evolves_to)
        print("Evolution>>", evolves_to[0]['species']['name'])

        for i in range(len(evolves_to)):
            evolutions.append(evolves_to[0]['species']['name'])
        return evolutions

    def datastore_list_pokemon(self, pokemon_list):
        saved = False
        # funcion para guardar la lista de los pokemones en el modelo
        for pokemon_data in pokemon_list:
            pokemon_db = PokemonModel(pokemon_id=pokemon_data['id'],
                                      pokemon_name=pokemon_data['name'],
                                      height=pokemon_data['height'],
                                      weight=pokemon_data['weight'],
                                      base_stats=pokemon_data['base_stats'],
                                      evolutions=pokemon_data['evolutions'],
                                      )
            pokemon_db.save()
        saved = True
        return saved








