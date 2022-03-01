import requests

ingredient = 'cheese'
def recipe_search(ingredient):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = '33ce055b'
    app_key = '4e8c57d880cb20934d9a6ab0fdafb620'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,

app_key)
)
data = result.json()
return data['hits']

def run():
ingredient = input('Enter an ingredient: ')
results = recipe_search(ingredient)
for result in results:
recipe = result['recipe']
print(recipe['label'])
print(recipe['uri'])
print()

run()