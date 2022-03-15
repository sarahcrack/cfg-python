import requests
import webbrowser

import pandas as pd

ingredient = input("Enter all ingredients separated by comma ")

# authentication and basic url with ingredients
application_id = '965b3663'
application_key = 'd64493bbe1e120fe6600dab019c5c932'
url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}'.format(ingredient, application_id,
                                                                                           application_key)


def input_meal_type():
    found_meal = False
    while found_meal == False:
        meal_allowed = ["breakfast", "lunch", "dinner", "teatime", "snack"]
        meal = input("What meal type are you looking for? breakfast, lunch, dinner, teatime or snack?")

        if meal in meal_allowed:
            found_meal = True
            meal_type_url = url + '&mealType={}'.format(meal)
            return meal_type_url
        elif meal == 'no' or bool(meal) == False:
            found_meal = True
            meal_type_url = url
            return meal_type_url
        else:
            print("invalid value entered, please type again")


def input_user_allergies():
    allergies = input("Are you allergic to anything? List ingredients separated by a comma or enter no ")

    if bool(allergies) == False or allergies == "no":
        allergies_url = input_meal_type()
        return allergies_url
    else:
        allergies_url = input_meal_type() + '&allergies={}'.format(allergies)
        return allergies_url


def input_user_calories():
    min_calories = input("What is the minimum calories? ")
    max_calories = input("What is the maximum calories? ")
    calories = min_calories + '-' + max_calories
    if bool(calories) == False or isinstance(min_calories, int) == 0 or isinstance(max_calories, int) == 0:
        calories_url = input_user_allergies()
        return calories_url
    else:
        calories_url = input_user_allergies() + '&calories={}'.format(calories)
        return calories_url


def input_user_time():
    max_time = input('What is maximum amount of time (in minutes) you want to spend cooking? ')
    if bool(max_time) == False or isinstance(max_time, int) == 0:
        time_url = input_user_calories()
        return time_url
    else:
        time = '1-{}'.format(max_time)
        time_url = input_user_calories() + '&time={}'.format(time)
        return time_url


def say_goodbye():
    print("thank you for using this service, goodbye.")


def print_the_results(recipes_dictionary):
    index = 0
    length_of_response = len(recipes_dictionary)
    while index < length_of_response:
        print(recipes_dictionary[index]['recipe']['label'])
        print(recipes_dictionary[index]['recipe']['url'])
        index += 1


def save_to_csv(final_list_of_recipes):
    df_recipes_all = pd.json_normalize(final_list_of_recipes, max_level=1)
    filtered_df = df_recipes_all[
        ['recipe.label', 'recipe.url', 'recipe.ingredientLines', 'recipe.totalTime',
         'recipe.cuisineType', 'recipe.dishType']]
    filtered_df.to_csv('recipes.csv')
    # return final_list_of_recipes


final_url = input_user_time()

response = requests.get(final_url)
response_code = response.status_code

# check the response from the API, if it's not ok then print the error and nothing else
if response.ok:
    all_recipes = response.json()
    number_of_recipes = all_recipes['count']
    if number_of_recipes > 20:
        print('there are {} recipes matching your criteria. Here\'s the top results:'.format(number_of_recipes))
    elif number_of_recipes > 0:
        print('there are {} recipes matching your criteria. Here\'s all results:'.format(number_of_recipes))
    else:
        print('there are {} recipes matching your criteria.'.format(number_of_recipes))

    recipes_all = all_recipes['hits']

    print_the_results(recipes_all)

    # check if the user can ask for more results
    in_page_results = all_recipes['to']

    overall_length = len(recipes_all)

    while overall_length < number_of_recipes:

        next_page = input("Do you want to see more results? y/n ")

        if next_page == 'y':
            next_url = all_recipes['_links']['next']['href']
            other_page = requests.get(next_url)
            more_recipes = other_page.json()

            # the last page doesn't have a next page url
            try:
                is_there_a_url = more_recipes['_links']['next']['href']
                next_url = more_recipes['_links']['next']['href']

                print('here are more results:')

                recipes_all_more = more_recipes['hits']
                recipes_all.extend(recipes_all_more)

                print_the_results(recipes_all_more)

                overall_length = len(recipes_all)
            except KeyError:
                print('here are more results:')

                recipes_all_more = more_recipes['hits']
                recipes_all.extend(recipes_all_more)

                print_the_results(recipes_all_more)

                overall_length = len(recipes_all)
                save = input("Do you want to save the current results? y/n ")
                if save == 'y':
                    save_to_csv(recipes_all)

        elif bool(next_page) == False or next_page == "n":
            save_results = input("Do you want to save the current results? y/n ")
            if save_results == 'y':
                save_to_csv(recipes_all)
            overall_length = number_of_recipes

    say_goodbye()
    overall_length = number_of_recipes

else:
    print(response)
    webbrowser.open('https://http.cat/{}.jpg'.format(response_code))
