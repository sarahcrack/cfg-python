import requests
from pprint import pprint


ingredient = input("What ingredients would you like to search for? ")
meal_type = input("What meal type are you looking for? breakfast, lunch, dinner, teatime or snack? ")
application_id = '33ce055b'
application_key = '4e8c57d880cb20934d9a6ab0fdafb620'
url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&mealType={}'.format(ingredient, application_id,
                                                                                   application_key,
                                                                                   meal_type)

response = requests.get(url)
# print(response)

recipes = response.json()
# print(all_recipes)

number_of_recipes = recipes['count']
print('There are {} recipes with your criteria. Here are the top results:'.format(number_of_recipes))

recipes_all = recipes['hits']

suitable_recipes = []


def meal_type():
    index = 0
    for item in recipes_all:
        recipe_name = item['recipe']['label']
        meal = item['recipe']['mealType']
        suitable_recipes.append({'name': recipe_name, 'meal type': meal})
        index += 1
        pprint('Recipe Name: {}, Meal Type: {}'.format(recipe_name, meal))


meal_type()


