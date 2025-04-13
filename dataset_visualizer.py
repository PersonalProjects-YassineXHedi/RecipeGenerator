import matplotlib.pyplot as plt
import pandas as pd

def ingredient_frequency_graph(df, first_n=80):
    """
    Visualizes the top 80 most common ingredients in a bar chart.

    Args:
        df_sorted_ingridient (pandas.DataFrame): A DataFrame that must contain 
            at least two columns: 'ingredient' (str) and 'count' (int), 
            sorted in descending order by 'count'.
        first_n (int): The number of top ingredients to display in the bar chart.

    Returns:
        None: Displays a bar chart of ingredient counts.
    """
    df_sorted_ingridient = sorted_ingridient_counter_df(df)
    df_sorted_ingridient = df_sorted_ingridient.head(first_n)
    plt.figure(figsize=(30, 10))
    plt.bar(df_sorted_ingridient['ingredients'], df_sorted_ingridient['count'])
    plt.xlabel('Ingredients', fontsize=6)
    plt.ylabel('Count')
    plt.title('Ingredient Count (Sorted)')
    plt.xticks(rotation=90, fontsize=6)
    #plt.tight_layout()
    plt.show()


def get_ingredient_count(df, ingredient):
    '''
    Retrieves the count of a specific ingredient from the sorted ingredient count DataFrame.

    Args:
        df (pd.DataFrame): A DataFrame with a column 'ingredients', where each row contains a list of strings.
        ingredient (str): The ingredient whose count you want to retrieve.

    Returns:
        int: The count of the specified ingredient, or 0 if the ingredient is not found.
    '''
    sorted_df = sorted_ingridient_counter_df(df)
    
    ingredient_count = sorted_df.loc[sorted_df['ingredients'] == ingredient, 'count']
    
    if not ingredient_count.empty:
        return ingredient_count.iloc[0]
    else:
        return 0

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