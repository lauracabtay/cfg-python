import requests
import time

# API call function
def ingredient_search(ingredient):
    app_key = 'a38175a5b6be0d443491d61a94398447'
    app_id = 'f58e9201'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    response = requests.get(url)
    # print(response)

    recipe_list = response.json()
    return recipe_list['hits']

# Function to print recipes
def recipe():

    # Getting user input for ingredient
    ingredient = input('Enter an ingredient: ')

    print('Let\'s look for some {} recipes!'.format(ingredient))
    time.sleep(2)

    # Ask user for number of max calories
    calories_filter = int(input('\nWhat is the maximum number of calories you would like the recipe to have? '))

    if calories_filter <= 500:
        print('That\'s healthy! Here are some {} recipes for under {} calories.'.format(ingredient, calories_filter))
    else:
        print('Need a bit of comfort? Here are {} recipes for under {} calories.'.format(ingredient, calories_filter))
    time.sleep(2)

    # Ask user for cuisine type
    cuisineType = input('\nWhat type of cuisine would you like? ').lower()

    if cuisineType == 'french':
        print('French cuisine! Bon appetit!')
    if cuisineType == 'italian':
        print('We have amazing italian recipes to show you pronto!')
    else:
        print('Let\'s have a look at some {} recipes.'.format(cuisineType))
    time.sleep(2)

    # API call assigned to a variable
    recipes = ingredient_search(ingredient)
    line_break = '\n'

    with open('recipes.txt', 'w+') as recipe_book:

        # Iterating through each recipe to get recipe name and url, using the API call variable

        for recipe in recipes:

            recipe_calories = int(recipe['recipe']['calories'])
            recipe_cuisineType = recipe['recipe']['cuisineType']
            i = 0
            while i < len(recipe_cuisineType):
                if cuisineType == recipe_cuisineType[i] and recipe_calories <= calories_filter:
                    # Display recipe name
                    recipe_label = recipe['recipe']['label'].upper()
                    print(line_break + recipe_label)

                    # Add recipe name to text file
                    recipe_book.write(recipe_label + line_break)

                    # Display recipe calories
                    print(recipe_calories, 'calories')

                    # Add recipe calories to text file
                    recipe_book.write(str(recipe_calories) + line_break)

                    # Display recipe cuisine
                    print(recipe_cuisineType[i], 'cuisine')

                    # Add recipe calories to text file
                    recipe_book.write(recipe_cuisineType[i] + ' cuisine' + line_break)

                    # Display recipe url
                    recipe_url = recipe['recipe']['url']
                    print(recipe_url)

                    # Add recipe url to text file
                    recipe_book.write(recipe_url + line_break)

                    # Retrieve recipe ingredients
                    ingredients = recipe['recipe']
                    ingredientLine = ingredients['ingredients']

                    # Iterating through each recipe's ingredients to get one ingredient by line
                    for ingredient in ingredientLine:

                        # Display recipe ingredients
                        recipe_ingredients = ingredient['text']
                        print(recipe_ingredients)

                        # Add recipe ingredients to text file
                        recipe_book.write(recipe_ingredients + line_break)
                i += 1

# Call recipe function
recipe()