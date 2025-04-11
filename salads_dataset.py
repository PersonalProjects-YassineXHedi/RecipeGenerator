import pandas as pd
from dataset_helper import change_df_tags_column_to_list, change_df_ingredients_column_to_list, create_salad_dataset

def get_salad_dataset(path_data_folder):
    return pd.read_csv(path_data_folder)

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



