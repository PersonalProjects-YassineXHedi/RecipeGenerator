import pandas as pd


def ingrident_counter(df):
    ingridients_and_count = {}
    for j in range(len(df)):
        list_ingredients = df.loc[j, 'ingredients']
        for ingredient in list_ingredients:
            if(ingredient in ingridients_and_count):
                ingridients_and_count[ingredient] += 1
            else:
                ingridients_and_count[ingredient] = 1
    sorted_dict = dict(sorted(ingridients_and_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def get_recipes_with_ingredients(ingredients, df):
    recipes_index = []
    for index, row in df.iterrows():
        if(check_recipe_with_ingredients(ingredients, row)):
            recipes_index.append(index)
    return recipes_index

def check_recipe_with_ingredients(ingredients, row):
    recipe_ingredients = row['ingredients']
    for ingredient in recipe_ingredients:
        if(ingredient not in ingredients):
            return False
    return True

def replace_row_ingredient_with_keywords(keywords, row):
    recipe_ingredients = row['ingredients']
    modified_ingredients = []
    for ingredient in recipe_ingredients:
        words = ingredient.split()
        was_replaced = False
        for keyword in keywords:
            if(keyword in words):
                modified_ingredients.append(keyword)
                was_replaced = True
                break
        if not was_replaced:
            modified_ingredients.append(ingredient)
    return modified_ingredients

def replace_df_ingredients_with_keywords(keywords, df):
    for index, row in df.iterrows():
        modified_ingredients = replace_row_ingredient_with_keywords(keywords,row)
        df.loc[index , 'ingredients'] = modified_ingredients
    return df 
    

def replace_row_ingredient_with_keywords(keywords, row):
    recipe_ingredients = row['ingredients']
    modified_ingredients = []
    for ingredient in recipe_ingredients:
        words = ingredient.split()
        was_replaced = False
        for keyword in keywords:
            if(keyword in words):
                modified_ingredients.append(keyword)
                was_replaced = True
                break
        if not was_replaced:
            modified_ingredients.append(ingredient)
    return modified_ingredients

def replace_row_ingredient_with_keywords(dict_old_new_value, row):
    recipe_ingredients = row['ingredients']
    modified_ingredients = []
    for ingredient in recipe_ingredients:
        if ingredient in dict_old_new_value:
            if(type(dict_old_new_value[ingredient]) is list):
                for elem in dict_old_new_value[ingredient]:
                    modified_ingredients.append(elem)
            else:
                modified_ingredients.append(dict_old_new_value[ingredient])
        else:
            modified_ingredients.append(ingredient)
    return modified_ingredients

def replace_df_ingredients_with_keywords(dict_old_new_value, df):
    for index, row in df.iterrows():
        modified_ingredients = replace_row_ingredient_with_keywords(dict_old_new_value,row)
        df.loc[index , 'ingredients'] = modified_ingredients
    return df 

def remove_keyword_from_ingredient_row(keywords_to_remove, row):
    recipe_ingredients = row['ingredients']
    modified_ingredients = []
    for ingredient in recipe_ingredients:
        words = ingredient.split()
        was_replaced = False
        for keyword in keywords_to_remove:
            if(keyword in words):
                new_words = []
                for word in words:
                    if word != keyword:
                        new_words.append(word)
                final_word = ' '.join(new_words).strip()
                modified_ingredients.append(final_word)
                was_replaced = True
                break
        if not was_replaced:
            modified_ingredients.append(ingredient)
    return modified_ingredients

def replace_df_ingredients_with_keywords(keywords_to_remove, df):
    for index, row in df.iterrows():
        modified_ingredients = remove_keyword_from_ingredient_row(keywords_to_remove,row)
        df.loc[index , 'ingredients'] = modified_ingredients
    return df 