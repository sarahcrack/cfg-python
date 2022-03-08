import requests
from pprint import pprint

ingredient = input("What ingredients would you like to search for? ")
application_id = '33ce055b'
application_key = '4e8c57d880cb20934d9a6ab0fdafb620'
url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, application_id, application_key)

response = requests.get(url)
# print(response)

all_recipes = response.json()
# print(all_recipes)

recipes_all = all_recipes['hits']
index = 0
while index < len(recipes_all):
    for key in recipes_all[index]:
        print(recipes_all[index]['recipe']['mealType'])
    index += 1

