import pandas as pd
from salads_dataset import create_salad_df_from_initial_df, save_df_csv
from dataset_helper import change_df_ingredients_column_to_list
pd.set_option('display.max_columns', None)     
pd.set_option('display.max_colwidth', None)     
pd.set_option('display.width', None)  

DATA_PATH = "C:/Users/yassi/Desktop/Projet/CookBotProject/CookBotRecipes/Data"

column_list = ['name', 'tags', 'description', 'ingredients']
df = create_salad_df_from_initial_df(DATA_PATH,column_list)
