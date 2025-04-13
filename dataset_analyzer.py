import pandas as pd
import matplotlib.pyplot as plt


def get_recipes_with_ingredients(ingredients, df):
    """
    Returns the indices of recipes in the dataframe that can be made with the list of ingredients provided.

    Args:
        ingredients (list): List of allowed ingredients.
        df (pd.DataFrame): DataFrame containing a column 'ingredients', which is a list of ingredients per recipe.

    Returns:
        list: Indices of the recipes that only contain the given ingredients.
    """
    recipes_index = []
    for index, row in df.iterrows():
        if(check_recipe_with_ingredients(ingredients, row)):
            recipes_index.append(index)
    return recipes_index

def get_df_filtered_without_list_ingredients(ingredients_to_remove, df):
    """
    Returns a DataFrame of recipes that do not contain any of the specified ingredients to remove.

    Args:
        ingredients_to_remove (list): List of ingredients that should be excluded.
        df (pd.DataFrame): DataFrame containing at least 'name' and 'ingredients' columns.

    Returns:
        pd.DataFrame: A filtered DataFrame containing only the recipes that do not include any of the ingredients to remove.
    """
    valid_indices = []
    for index, row in df.iterrows():
        if not is_row_to_remove(ingredients_to_remove, row):
            valid_indices.append(index)
    return df.loc[valid_indices].reset_index(drop=True)


def replace_df_ingredients_with_keywords(keywords, df):
    """
    Replaces ingredients in all the DataFrame using matching keywords. When the keyword (single word)
    is found in an ingredient (multiple words) the old ingredient is replaced by the keyword.

    Args:
        keywords (list): List of keywords to match and replace.
        df (pd.DataFrame): DataFrame with a column 'ingredients' containing ingredient lists.

    Returns:
        pd.DataFrame: Updated DataFrame with modified ingredients.
    """
    for index, row in df.iterrows():
        modified_ingredients = replace_row_ingredient_with_keywords(keywords,row)
        df.loc[index , 'ingredients'] = modified_ingredients
    return df 

def replace_old_ingredients_with_new_df(dict_old_new_value, df):
    """
    Replaces ingredients in the DataFrame based on a mapping dictionary. Method search for ingredients (keys in dict)
    and replace them with new ingredients (values in dict)

    Args:
        dict_old_new_value (dict): Dictionary mapping original ingredient strings to new values (str or list).
        df (pd.DataFrame): DataFrame with a column 'ingredients'.

    Returns:
        pd.DataFrame: Updated DataFrame with replaced ingredients.
    """
    for index, row in df.iterrows():
        modified_ingredients = replace_old_ingredients_with_new_row(dict_old_new_value,row)
        df.loc[index , 'ingredients'] = modified_ingredients
    return df 

def remove_keywords_from_ingredients_df(keywords_to_remove, df):
    """
    Removes specified keywords from the ingredients of the DataFrame.

    Args:
        keywords_to_remove (list): List of keywords to remove from ingredients.
        df (pd.DataFrame): DataFrame with a column 'ingredients'.

    Returns:
        pd.DataFrame: Updated DataFrame with keywords removed from ingredients.
    """
    for index, row in df.iterrows():
        modified_ingredients = remove_keyword_from_ingredient_row(keywords_to_remove,row)
        df.loc[index , 'ingredients'] = modified_ingredients
    return df 

def get_all_words_in_ingredients_df(df):
    """
    Extracts all words from the 'ingredients' column across all rows in the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with an 'ingredients' column containing lists of ingredient strings.

    Returns:
        list: A combined list of all words found in the ingredients of the entire DataFrame.
    """
    all_words = []
    for index, row in df.iterrows():
        row_words = get_all_words_in_ingredients_row(row)
        for word in row_words:
            all_words.append(word)
    return all_words

def get_all_diff_ingredients_with_keyword_df(keyword, df):
    """
    Retrieves all ingredient strings from the DataFrame that contain a given keyword.

    Args:
        keyword (str): Keyword to search for in ingredient strings.
        df (pd.DataFrame): DataFrame containing an 'ingredients' column (list of strings per row).

    Returns:
        list: A list of unique ingredient strings that contain the specified keyword.
    """
    ingredients_containing_keyword = []
    for index,row in df.iterrows():
        ingredients_list = row['ingredients']
        for ingredient in ingredients_list:
            if(keyword in ingredient):
                ingredients_containing_keyword.append(ingredient)
    return ingredients_containing_keyword


#Private method

def check_recipe_with_ingredients(ingredients, row):
    """
    Private method

    Checks whether all ingredients in a recipe are contained in the given list.

    Args:
        ingredients (list): List of allowed ingredients.
        row (pd.Series): A row from the DataFrame with a key 'ingredients'.

    Returns:
        bool: True if all ingredients in the recipe are allowed, False otherwise.
    """
    recipe_ingredients = row['ingredients']
    for ingredient in recipe_ingredients:
        if(ingredient not in ingredients):
            return False
    return True

def replace_row_ingredient_with_keywords(keywords, row):
    """
    Private method

    Replaces words in each ingredient of the row with a matching keyword if found.

    Args:
        keywords (list): List of keywords to match and replace.
        row (pd.Series): A row from the DataFrame with a key 'ingredients'.

    Returns:
        list: Modified list of ingredients where matching words are replaced with the keyword.
    """
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

def replace_old_ingredients_with_new_row(dict_old_new_value, row):
    """
    Private method

    Try to replace ingredients in a row based on a mapping dictionary. Method searches for ingredients (keys in dict)
    and replace them with new ingredients (values in dict)

    Args:
        dict_old_new_value (dict): Dictionary mapping original ingredient strings to new values (str or list).
        row (pd.Series): A row from the DataFrame with a key 'ingredients'.

    Returns:
        list: Modified ingredient list with replacements.
    """
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
    modified_ingredients = list(set(modified_ingredients))
    return modified_ingredients

def remove_keyword_from_ingredient_row(keywords_to_remove, row):
    """
    Private method

    Removes specified keywords if present from each ingredient in the given row .

    Args:
        keywords_to_remove (list): List of keywords to be removed from the ingredients.
        row (pd.Series): A row from the DataFrame with a key 'ingredients'.

    Returns:
        list: Modified ingredient list with specified keywords removed.
    """
    recipe_ingredients = row['ingredients']
    modified_ingredients = []
    for ingredient in recipe_ingredients:
        words = ingredient.split()
        was_replaced = False
        new_ingredient_words = []
        for word in words:
            if word not in keywords_to_remove:
                new_ingredient_words.append(word)
        final_word = ' '.join(new_ingredient_words).strip()
        modified_ingredients.append(final_word)
    return modified_ingredients

<<<<<<< Updated upstream
=======
def sorted_ingridient_counter_df(df):
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


def get_all_words_in_ingredients_row(row):
    """
    Private method

    Extracts all individual words from the ingredients of a single row.

    Args:
        row (pd.Series): A row from the DataFrame containing an 'ingredients' column as a list of strings.

    Returns:
        list: A list of all words found in the ingredient strings of the row.
    """
    row_words = []
    recipe_ingredients = row['ingredients']
    for ingredient in recipe_ingredients:
        words = ingredient.split()
        for word in words:
            row_words.append(word)
    return row_words


def is_row_to_remove(ingredients_to_remove, row):
    recipe_ingredients = row['ingredients']
    for ingredient in recipe_ingredients:
        if ingredient in ingredients_to_remove:
            return True
    return False
>>>>>>> Stashed changes
