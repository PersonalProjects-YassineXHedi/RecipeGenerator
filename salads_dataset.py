import pandas as pd
from dataset_helper import change_df_tags_column_to_list, change_df_ingredients_column_to_list, create_salad_dataset

DATA_PATH_HEDI = "/home/hboua/GitRepo/Data"
DATA_PATH_YASSINE = "C:/Users/yassi/Desktop/Projet/CookBotProject/CookBotRecipes/Data"

def get_salad_dataset(path_data_folder):
    recipes_file_path = path_data_folder + "/salad_dataset.csv"
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

def ingredient_counter_on_df(df):
    change_df_ingredients_column_to_list(df)
    ingridients_and_count = []
    # iterate through the rows of the dataframe
    for j in range(len(df)):
        list_ingredients = df.loc[j, 'ingredients']
        # iterate through the list of ingredients
        for i in range (len(list_ingredients)):
            does_not_exist_in_list = True
            ingridient = list_ingredients[i]
            # check if the ingredient is already in the list
            for ingridient_dic in ingridients_and_count:
                if ingridient in ingridient_dic:
                    does_not_exist_in_list = False
                    ingridient_dic[ingridient] += 1
                    break
            # if not in list append
            if does_not_exist_in_list:
                ingridients_and_count.append({ingridient: 1})
    ingridients_and_count = sorted(ingridients_and_count, key=lambda d: list(d.values())[0], reverse=True)
    return ingridients_and_count 

def matching_ingredient_counter_on_row(ingredients, row):
    list_ingredients = row['ingredients']
    count = 0
    for ingredient in list_ingredients:
        if(ingredient in ingredients):
            count += 1
    return count

def matching_tags_counter_on_row(tags, row):
    list_tags = row['tags']
    count = 0
    for tag in list_tags:
        if(tag in tags):
            count += 1
    return count

def matching_ingredient_counter_on_df(ingredients, df):
    matching_ingredient_df = {}
    for index, row in df.iterrows():
        count = matching_ingredient_counter_on_row(ingredients, row)
        matching_ingredient_df[index] = count
    sorted_dict = dict(sorted(matching_ingredient_df.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
        


            
    



