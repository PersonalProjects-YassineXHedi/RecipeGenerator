import pandas as pd
pd.set_option('display.max_columns', None)     
pd.set_option('display.max_colwidth', None)     
pd.set_option('display.width', None)  

def get_all_available_tags(df):
    """
    Extracts all unique tags from the 'tags' column of the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing a 'tags' column with string-encoded tags.

    Returns:
        list: A list of unique tags found in the DataFrame.
    """
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

def change_df_tags_column_to_list(df):
    """
    Converts the 'tags' column in the DataFrame from a string format to a list of strings, in-place.

    Args:
        df (pd.DataFrame): DataFrame containing a 'tags' column in string format.

    Returns:
        None
    """

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
    """
    Filters the DataFrame to only include rows where at least one tag is in the provided tags list.

    Args:
        df (pd.DataFrame): DataFrame with a 'tags' column.
        tags_list (list): Tags to filter by.

    Returns:
        pd.DataFrame: Filtered DataFrame with duplicates removed based on the 'name' column.
    """
    filtered = df[df['tags'].apply(lambda tags: any(tag in tags for tag in tags_list) if isinstance(tags, list) else False)]
    return filtered.drop_duplicates(subset='name')

def get_row_ids_containing_salad_in_name(df):
    """
    Retrieves row indices where the 'name' column contains the word 'salad'.

    Args:
        df (pd.DataFrame): DataFrame with a 'name' column.

    Returns:
        list: List of row indices where 'salad' appears in the name.
    """
    df_containing_salad_in_name = df[df['name'].str.contains('salad', case=False, na=False)]
    ids_rows_containing_salad_in_name = []
    for index, row in df_containing_salad_in_name.iterrows():
        ids_rows_containing_salad_in_name.append(index)
    return ids_rows_containing_salad_in_name

def get_row_ids_containing_salads_as_tag(df):
    """
    Retrieves row indices where 'salads' is one of the tags.

    Args:
        df (pd.DataFrame): DataFrame with a 'tags' column containing lists.

    Returns:
        list: List of row indices where 'salads' is present in the tags.
    """
    ids_rows_containing_salads_as_tag = []
    for index, row in df.iterrows():
        if( ('salads' in row['tags'])):
            ids_rows_containing_salads_as_tag.append(index)
    return ids_rows_containing_salads_as_tag

def get_row_ids_containing_salad_in_name_or_as_tag(df):
    """
    Combines row indices from both 'salad' in name and 'salads' in tags.

    Args:
        df (pd.DataFrame): DataFrame with 'name' and 'tags' columns.

    Returns:
        list: Unique list of row indices that match either condition.
    """
    ids_rows_containing_salad_in_name_or_as_tag = []
    df_containing_salad_in_name = df[df['name'].str.contains('salad', case=False, na=False)]
    for index, row in df_containing_salad_in_name.iterrows():
        ids_rows_containing_salad_in_name_or_as_tag.append(index)
    for index, row in df.iterrows():
        if( ('salads' in row['tags'])):
            ids_rows_containing_salad_in_name_or_as_tag.append(index)
    return list(set(ids_rows_containing_salad_in_name_or_as_tag))

def create_salad_dataset(df):
    """
    Creates a new DataFrame containing only the rows related to salads, based on name or tags.

    Args:
        df (pd.DataFrame): Original DataFrame.

    Returns:
        pd.DataFrame: Filtered DataFrame containing only salad-related rows.
    """
    index_list = get_row_ids_containing_salad_in_name_or_as_tag(df)
    return df.loc[index_list].reset_index(drop=True)

def change_df_ingredients_column_to_list(df):
    """
    Converts the 'ingredients' column in the DataFrame from a string format to a list of strings, in-place.

    Args:
        df (pd.DataFrame): DataFrame containing an 'ingredients' column in string format.

    Returns:
        None
    """
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
