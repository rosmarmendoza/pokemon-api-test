import requests
import pprint as pp

''' Class PokeApi Service
    this class allows encapsulate the 
    communication layer and type communication
'''


class PokeApiService:
    url_base = ''
    connection_type = ''
    client = None

    def __init__(
            self,
            url_base="https://pokeapi.co/api/v2/",
            connection_type="request"
    ):
        if connection_type != "request":
            raise Exception("Connection not allow")

        self.url_base = url_base
        self.connection_type = connection_type
        self.client = requests

    ''' Abstraction for build the connection 
     to the PokeApi Evolution Chain endpoint '''

    def chain_evolution(self, evolution_chain_id):

        evolution_endpoint_url =\
            f"{self.url_base}evolution-chain/{evolution_chain_id}"
        # print("<< URL evolution_endpoint>>")
        evolution_response = self.client.get(evolution_endpoint_url)
        # print(evolution_response)
        
        if evolution_response.status_code == 200:
            evolution_chain_info = evolution_response.json()
            return evolution_chain_info

        raise Exception("Error with the input for command evolution-chain",
                        evolution_chain_id)
    ''' Abstraction for build the connection 
     to the PokeApi Pokemon endpoint '''

    def pokemon_info(self, pokemon_name):
        pokemon_url = f"{self.url_base}pokemon/{pokemon_name}"  # Pokemon URL
        # print("<< URL POKEMON  OK >>")
        pokemon_response = requests.get(pokemon_url)
        if pokemon_response.status_code == 200:
            pokemon_info = pokemon_response.json()
            return pokemon_info

        raise Exception("Pokemon data not found")
