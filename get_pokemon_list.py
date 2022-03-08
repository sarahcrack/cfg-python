import requests
from pprint import pprint

pokemon_number = [2, 11, 22, 33, 44, 55]
data = {}

for num in pokemon_number:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(num)

    response = requests.get(url)
    pokemon = response.json()

    name = pokemon['name']
    data['name'] = name

    moves = pokemon['moves']
    moves_data = []
    for move in moves:
        moves_data.append(move['move']['name'])
    data['moves'] = moves_data

pprint(data)

with open('pokemon.txt', 'w+') as pokemons:
    pokemon_info = pokemons.write(str(data))


