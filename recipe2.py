import requests
from pprint import pprint

ingredient = input("What ingredients would you like to search for? ")
application_id = '33ce055b'
application_key = '4e8c57d880cb20934d9a6ab0fdafb620'
url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, application_id, application_key)

response = requests.get(url)
print(response)

all_recipes = response.json()
pprint(all_recipes)
