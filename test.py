import pandas as pd
from salads_dataset import create_salad_df_from_initial_df, matching_tags_counter_on_df, matching_tags_counter_on_row, matching_ingredient_counter_on_df, matching_ingredient_counter_on_row

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

tags = ['preparation', 'beef']

sorted_dict = matching_tags_counter_on_df(tags, df )

count = 0
for elem in sorted_dict :
    count += 1
    if count == 100:
        break
    x = f"{elem} : {sorted_dict[elem]}"
    print(x)
