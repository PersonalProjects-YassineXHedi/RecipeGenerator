import matplotlib.pyplot as plt
import pandas as pd

def ingredient_frequency_graph(df):
    """
    Visualizes the top 80 most common ingredients in a horizontal bar chart with labels.

    Args:
        df (pandas.DataFrame): Must have 'ingredients' and 'count' columns.

    Returns:
        None
    """
    df_sorted_ingridient = sorted_ingridient_counter_df(df)
    df_sorted_ingridient = df_sorted_ingridient.head(80)

    plt.figure(figsize=(10, 10))  # Adjust width and height
    plt.barh(df_sorted_ingridient['ingredients'], df_sorted_ingridient['count'], color='steelblue')
    plt.xlabel('Count')
    plt.ylabel('Ingredients')
    plt.title('Top 80 Ingredient Counts')

    # Add labels to each bar
    for i, (count) in enumerate(df_sorted_ingridient['count']):
        plt.text(count + 1, i,str(count) , va='center', fontsize=6)

    plt.gca().invert_yaxis()  # So the highest count is at the top
    plt.tight_layout()
    plt.show()


# private method
def sorted_ingridient_counter_df(df):
    '''

    Private methods

    Counts how often each ingredient appears in the 'ingredients' column and returns a sorted DataFrame.

    Args:
        df (pd.DataFrame): A DataFrame with a column 'ingredients', where each row contains a list of strings.

    Returns:
        pd.DataFrame: A DataFrame with columns 'ingredient' and 'count', sorted by count in descending order.
    '''
    df_ingredient = {
        "ingredients":[],
        "count":[]
    }

    for j in range(len(df)):
        list_ingredients = df.loc[j, 'ingredients']
        for i in range (len(list_ingredients)):
            not_found = True
            ingredient = list_ingredients[i]
            for _ in list_ingredients:
                if ingredient in df_ingredient["ingredients"]:
                    not_found = False
                    index = df_ingredient["ingredients"].index(ingredient)
                    df_ingredient["count"][index] += 1
                    break
            if not_found:
                df_ingredient["ingredients"].append(ingredient)
                df_ingredient["count"].append(1)

    df_ingredient = pd.DataFrame(df_ingredient)   
    df_sorted = df_ingredient.sort_values(by=['count'], ascending=False)   
    return df_sorted

def get_ingredients_after_top_n_from_ing_count_df(n, df):
    """
    Extracts the first n ingredient names from a DataFrame containing an 'ingredients' column.

    Args:
        n (int): The number of ingredient names to extract.
        df (pd.DataFrame): A DataFrame with a column named 'ingredients' 
                           containing ingredient names (typically sorted by frequency).

    Returns:
        list: A list containing the first n ingredient names from the DataFrame.
    """
    sorted_list_ingredients = df['ingredients']
    chosen_ingredients = []
    i=0
    for ingredient in sorted_list_ingredients:
        i +=1
        if(i <= n):
            continue
        chosen_ingredients.append(ingredient)
    return chosen_ingredients
    

    