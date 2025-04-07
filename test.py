import pandas as pd
from datasetAnalysis import change_df_tags_column_to_list, get_dataset_with_specific_tags
pd.set_option('display.max_columns', None)     
pd.set_option('display.max_colwidth', None)     
pd.set_option('display.width', None)  


DATA_PATH = "C:/Users/yassi/Desktop/Projet/CookBotProject/CookBotRecipes/Data/archive/RAW_recipes.csv"


df = pd.read_csv(DATA_PATH)
len(df)

column_df = df[['name', 'tags', 'description']]
change_df_tags_column_to_list(column_df)


salad_tags = ['salads', 'vegetables', 'side-dishes', 'no-cook', 'easy', 'healthy', 'served-cold', 'vegetarian']

salad_df = get_dataset_with_specific_tags(column_df,salad_tags)


rows_containing_salad_in_name = salad_df[salad_df['name'].str.contains('salad', case=False, na=False)]

ids_rows_containing_either_one_or_other = []

ids_rows_containing_salad_in_name = []
for index, row in rows_containing_salad_in_name.iterrows():
    ids_rows_containing_salad_in_name.append(index)
    ids_rows_containing_either_one_or_other.append(index)

ids_rows_containing_salads_as_tag = []
for index, row in salad_df.iterrows():
    if( ('salads' in row['tags'])):
        ids_rows_containing_salads_as_tag.append(index)
        ids_rows_containing_either_one_or_other.append(index)

ids_rows_containing_either_one_or_other = list(set(ids_rows_containing_either_one_or_other))
len(ids_rows_containing_either_one_or_other)
ids_row_with_name_not_tags = []
ids_row_with_tags_not_name = []
ids_row_in_one_not_other = []

for id in ids_rows_containing_salad_in_name:
    if(id not in ids_rows_containing_salads_as_tag):
        ids_row_with_name_not_tags.append(id)
        ids_row_in_one_not_other.append(id)

for id in ids_rows_containing_salads_as_tag:
    if(id not in ids_rows_containing_salad_in_name):
        ids_row_with_tags_not_name.append(id)
        ids_row_in_one_not_other.append(id)

len(ids_row_with_name_not_tags)
len(ids_row_with_tags_not_name)
len(ids_row_in_one_not_other)

new_df = create_salad_dataset(column_df)
len(new_df)