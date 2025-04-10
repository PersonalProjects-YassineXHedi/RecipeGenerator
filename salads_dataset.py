import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dataset_helper import change_df_tags_column_to_list, change_df_ingredients_column_to_list, create_salad_dataset

DATA_PATH = "/home/hboua/GitRepo/Data"
def get_salad_dataset(path_data_folder):
    recipes_file_path = path_data_folder + "/salad_dataset.csv"
    print(recipes_file_path)
    return pd.read_csv(recipes_file_path)

def get_dataset_with_specific_columns(df, column_list):
    return df[column_list]

def create_salad_df_from_initial_df(path_data_folder, column_list):
    df = get_salad_dataset(path_data_folder)
    df = get_dataset_with_specific_columns(df,column_list)
    change_df_tags_column_to_list(df)
    change_df_ingredients_column_to_list(df)
    return create_salad_dataset(df)


def save_df_csv(df, file_name, path_data_folder):
    file_path = path_data_folder + '/' + file_name + '.csv'
    df.to_csv(file_path, index=False)

def df_sorted_ingridient(df=get_salad_dataset(DATA_PATH)):
    change_df_ingredients_column_to_list(df)
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

def visulize_ingridient(df_sorted_ingridient=df_sorted_ingridient(get_salad_dataset(DATA_PATH))):
   
    df_sorted_ingridient = df_sorted_ingridient.head(80)
    plt.figure(figsize=(20, 8))
    plt.bar(df_sorted_ingridient['ingredient'], df_sorted_ingridient['count'])
    plt.xlabel('Ingredient', fontsize=6)
    plt.ylabel('Count')
    plt.title('Ingredient Count (Sorted)')
    plt.xticks(rotation=90, fontsize=6)
    
    plt.tight_layout()
    plt.show()



# visulize_ingridient(df_sorted_ingridient(get_salad_dataset(DATA_PATH)))


