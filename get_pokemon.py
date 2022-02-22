import requests
from pprint import pprint
# pretty print

# ask user for input so we know what data to grab
pokemon_number = input("What is the Pokemon's ID? ")

# the Pokemon ID number goes into the curly brackets
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

# how to access the information in a certain file format (turning lots of text into a more readable format)
pokemon = response.json()
pprint(pokemon['name'])
pprint(pokemon['height'])
pprint(pokemon['weight'])
pprint(pokemon)
