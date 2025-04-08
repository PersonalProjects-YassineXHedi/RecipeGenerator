import pandas as pd
pd.set_option('display.max_columns', None)     
pd.set_option('display.max_colwidth', None)     
pd.set_option('display.width', None)  

DATA_PATH = "C:/Users/yassi/Desktop/Projet/CookBotProject/CookBotRecipes/Data/archive/RAW_recipes.csv"

def get_all_available_tags(df):
    available_tag = []
    for j in range(len(df)):
        tags_chars = df.loc[j, 'tags']
        i = 0
        while(i < len(tags_chars)):
            if(tags_chars[i] == "'"):
                i += 1
                char_tag = []
                while(tags_chars[i] != "'"):
                    char_tag.append(tags_chars[i])
                    i += 1
                tag = ''.join(char_tag)
                available_tag.append(tag)
                i +=1
            else:
                i += 1 
    available_tag = list(set(available_tag))
    return available_tag

def get_important_column_df(df, column_names = ['name', 'tags', 'description']):
    return df[column_names]

def change_df_tags_column_to_list(df):
    if(type(df.loc[0,'tags']) == list):
        return
    for j in range(len(df)):
        tags_chars = df.loc[j, 'tags']
        tags_list = []
        i = 0
        while(i < len(tags_chars)):
            if(tags_chars[i] == "'"):
                i += 1
                char_tag = []
                while(tags_chars[i] != "'"):
                    char_tag.append(tags_chars[i])
                    i += 1
                tag = ''.join(char_tag)
                tags_list.append(tag)
                i +=1
            else:
                i += 1 
        df.loc[j, 'tags'] = tags_list

def get_dataset_with_specific_tags(df, tags_list):
    filtered = df[df['tags'].apply(lambda tags: any(tag in tags for tag in tags_list) if isinstance(tags, list) else False)]
    return filtered.drop_duplicates(subset='name')

def get_row_ids_containing_salad_in_name(df):
    df_containing_salad_in_name = df[df['name'].str.contains('salad', case=False, na=False)]
    ids_rows_containing_salad_in_name = []
    for index, row in df_containing_salad_in_name.iterrows():
        ids_rows_containing_salad_in_name.append(index)
    return ids_rows_containing_salad_in_name

def get_row_ids_containing_salads_as_tag(df):
    ids_rows_containing_salads_as_tag = []
    for index, row in df.iterrows():
        if( ('salads' in row['tags'])):
            ids_rows_containing_salads_as_tag.append(index)
    return ids_rows_containing_salads_as_tag

def get_row_ids_containing_salad_in_name_or_as_tag(df):
    ids_rows_containing_salad_in_name_or_as_tag = []
    df_containing_salad_in_name = df[df['name'].str.contains('salad', case=False, na=False)]
    for index, row in df_containing_salad_in_name.iterrows():
        ids_rows_containing_salad_in_name_or_as_tag.append(index)
    for index, row in df.iterrows():
        if( ('salads' in row['tags'])):
            ids_rows_containing_salad_in_name_or_as_tag.append(index)
    return list(set(ids_rows_containing_salad_in_name_or_as_tag))

def create_salad_dataset(df):
    index_list = get_row_ids_containing_salad_in_name_or_as_tag(df)
    return df.loc[index_list].reset_index(drop=True)

def change_df_ingredients_column_to_list(df):
    if(type(df.loc[0,'ingredients']) == list):
        return
    for j in range(len(df)):
        ingredients_chars = df.loc[j, 'ingredients']
        ingredients_list = []
        i = 0
        while(i < len(ingredients_chars)):
            if(ingredients_chars[i] == "'"):
                i += 1
                char_tag = []
                while(ingredients_chars[i] != "'"):
                    char_tag.append(ingredients_chars[i])
                    i += 1
                tag = ''.join(char_tag)
                ingredients_list.append(tag)
                i +=1
            else:
                i += 1 
        df.loc[j, 'ingredients'] = ingredients_list
