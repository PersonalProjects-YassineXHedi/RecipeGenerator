import pandas as pd
import sqlite3
import os 

from dataset_helper import change_df_tags_column_to_list, change_df_ingredients_column_to_list, create_salad_dataset

def create_salad_df_from_initial_df(path_data_folder, column_list = ['name', 'tags', 'description', 'ingredients']):
    """
    Creates a DataFrame filtered with specific columns.

    This function loads a dataset from the given folder path, selects only the specified columns,
    converts string-encoded tags and ingredients to lists, and filters the rows related to salads.

    Args:
        path_data_folder (str): Path to the folder containing the dataset file.
        column_list (list, optional): List of columns to keep in the final DataFrame. 
                                      Defaults to ['name', 'tags', 'description', 'ingredients'].

    Returns:
        pd.DataFrame: A DataFrame containing only salad-related rows and the selected columns.
    """
    df = get_salad_dataset(path_data_folder)
    df = get_dataset_with_specific_columns(df,column_list)
    change_df_tags_column_to_list(df)
    change_df_ingredients_column_to_list(df)
    return create_salad_dataset(df)


def save_df_csv(df, file_name, path_data_folder):
    """
    Saves a DataFrame to a CSV file in the specified folder.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_name (str): Name of the CSV file (without extension).
        path_data_folder (str): Path to the folder where the file will be saved.

    Returns:
        None
    """
    file_path = path_data_folder + '/' + file_name + '.csv'
    df.to_csv(file_path, index=False)

def tranform_df_from_csv_to_sqlite(path_data_folder, file_name):
    """
    Loads a CSV file as a DataFrame and saves it as a SQLite database in the specified path.

    Args:
        path_data_folder (str): Path to the folder containing the CSV file.
        file_name (str): Name of the CSV file (without extension) and target database name.

    Returns:
        None
    """
    df = get_salad_dataset(path_data_folder, file_name)
    db_path = os.path.join(path_data_folder, file_name + '.db')
    connexion = sqlite3.connect(db_path)
    df.to_sql("recipes_v1", connexion, if_exists="replace", index=False)


#private methods

def get_salad_dataset(path_data_folder, file_name):
    '''
        Private method

        Loads the base salad dataset from a CSV file.

        Args:
            path_data_folder (str): Path to the folder containing the dataset.
            file_name (str): Name of the CSV file (without extension).

        Returns:
            pd.DataFrame: The loaded DataFrame from csv file.
    '''
    recipes_file_path = path_data_folder + "/"+ file_name+".csv"
    return pd.read_csv(recipes_file_path)

def get_dataset_with_specific_columns(df, column_list):
    '''
        Private method

        Selects specific columns from the provided DataFrame.

        Args:
            df (pd.DataFrame): Original DataFrame.
            column_list (list): List of column names to keep.

        Returns:
            pd.DataFrame: Reduced DataFrame with only the specified columns.
    '''
    return df[column_list]



def add_column_to_current_df(raw_df, df, column_name_list_added, common_collumn_name):
    '''
    Private methods

    Adds a new column from a raw DataFrame to the existing DataFrame by merging on a common column.

    Args:
        raw_df (pd.DataFrame): DataFrame containing the column to add.
        df (pd.DataFrame): The original DataFrame to which the column will be added.
        column_name_added (str): Name of the column in raw_df to add to df.
        common_collumn_name (list): Common columns to both DataFrames to perform the merge on.

    Returns:
        pd.DataFrame: Updated DataFrame with the new column added.
    '''
    input = df 
    for column in  column_name_list_added:
        output = pd.merge(input, raw_df[[*common_collumn_name, column]],on=common_collumn_name, how='left')
        input = output
    return output