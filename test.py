import pandas as pd
from salads_dataset import create_salad_df_from_initial_df, get_salad_dataset, matching_ingredient_counter_on_df, matching_ingredient_counter_on_row

pd.set_option('display.max_columns', None)     
pd.set_option('display.max_colwidth', None)     
pd.set_option('display.width', None)  \

DATA_PATH_HEDI = "/home/hboua/GitRepo/Data"
DATA_PATH_YASSINE = "C:/Users/yassi/Desktop/Projet/CookBotProject/CookBotRecipes/Data"
'''
column_list = ['name', 'tags', 'description', 'ingredients']
df = create_salad_df_from_initial_df(DATA_PATH,column_list)
'''
column_list = ['name', 'tags', 'description', 'ingredients']
df = create_salad_df_from_initial_df(DATA_PATH_YASSINE, column_list)

ingredients  = ['olive oil', 'purple onion', 'red potatoes']

# row = df.loc[0,'ingredients']
# row
# ct = matching_ingredient_counter_on_row(ingredients, row)

# for index, row in df.iterrows():
#     count = matching_ingredient_counter_on_row(ingredients, row)
#     print(count)
#     break
    


# list_ingredients = row['ingredients']
# count = 0
# for ingredient in list_ingredients:
#     if(ingredient in ingredients):
#         count += 1

match_dict   = matching_ingredient_counter_on_df(ingredients, df)

count = 0
for elem in match_dict :
    count += 1
    if count == 100:
        break
    x = f"{elem} : {match_dict[elem]}"
    print(x)
