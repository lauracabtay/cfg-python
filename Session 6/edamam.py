import requests

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

    # API call assigned to a variable
    recipes = ingredient_search(ingredient)
    line_break = '\n'

    # Iterating through each recipe to get recipe name and url, using the API call variable
    for recipe in recipes:

        # Display recipe name
        recipe_label = recipe['recipe']['label'].upper()
        print(recipe_label)

        # Add recipe name to text file
        with open('recipes.txt', 'a+') as recipe_book:
            recipe_book.write(recipe_label + line_break)

        # Display recipe url
        recipe_url = recipe['recipe']['url']
        print(recipe_url)

        # Add recipe url to text file
        with open('recipes.txt', 'a+') as recipe_book:
            recipe_book.write(recipe_url + line_break)

        # Iterating through each recipe's ingredients to get one ingredient by line
        ingredients = recipe['recipe']
        ingredientLine = ingredients['ingredients']

        for ingredient in ingredientLine:
            # Display recipe ingredients
            recipe_ingredients = ingredient['text']
            print(recipe_ingredients)

            # Add recipe ingredients to text file
            with open('recipes.txt', 'a+') as recipe_book:
                recipe_book.write(recipe_ingredients + line_break)

        print(line_break)
        with open('recipes.txt', 'a+') as recipe_book:
            recipe_book.write(line_break)

# Call recipe function
recipe()