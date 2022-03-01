import requests
from pprint import pprint

pokemon_number = [2, 11, 22, 33, 44, 55]

for num in pokemon_number:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(num)

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon['name'])

