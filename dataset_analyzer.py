import pandas as pd
import matplotlib.pyplot as plt


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

def sorted_ingridient_counter_df(df):
    '''
    Counts how often each ingredient appears in the 'ingredients' column and returns a sorted DataFrame.

    Args:
        df (pd.DataFrame): A DataFrame with a column 'ingredients', where each row contains a list of strings.

    Returns:
        pd.DataFrame: A DataFrame with columns 'ingredient' and 'count', sorted by count in descending order.
    '''
    df_ingredient = {
        "ingredient":[],
        "count":[]
    }

    # iterate through the rows of the dataframe
    for j in range(len(df)):
        list_ingredients = df.loc[j, 'ingredients']
        # iterate through the list of ingredients
        for i in range (len(list_ingredients)):
            not_found = True
            ingredient = list_ingredients[i]
            # check if the ingredient is already in the list
            for item in list_ingredients:
                if ingredient in df_ingredient["ingredient"]:
                    not_found = False
                    index = df_ingredient["ingredient"].index(ingredient)
                    df_ingredient["count"][index] += 1
                    break
            # if not in list append
            if not_found:
                df_ingredient["ingredient"].append(ingredient)
                df_ingredient["count"].append(1)

    df_ingredient = pd.DataFrame(df_ingredient)   
    df_sorted = df_ingredient.sort_values(by=['count'], ascending=False)   
    return df_sorted

def visulize_ingridient(df_sorted_ingridient):
     """
    Visualizes the top 80 most common ingredients in a bar chart.

    Args:
        df_sorted_ingridient (pandas.DataFrame): A DataFrame that must contain 
            at least two columns: 'ingredient' (str) and 'count' (int), 
            sorted in descending order by 'count'.

    Returns:
        None: Displays a bar chart of ingredient counts.
    """
     
    df_sorted_ingridient = df_sorted_ingridient.head(80)
    plt.figure(figsize=(20, 8))
    plt.bar(df_sorted_ingridient['ingredient'], df_sorted_ingridient['count'])
    plt.xlabel('Ingredient', fontsize=6)
    plt.ylabel('Count')
    plt.title('Ingredient Count (Sorted)')
    plt.xticks(rotation=90, fontsize=6)
    plt.tight_layout()
    plt.show()