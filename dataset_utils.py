import pandas as pd

def elem_counter_list(list):
    """
    Counts the frequency of each element in a list and returns a dictionary sorted by count in descending order.

    Args:
        list (list): A list of elements to count.

    Returns:
        dict: A dictionary where keys are the unique elements from the list, and values are their corresponding counts,
              sorted in descending order of frequency.
    """
    elems_and_count = {}
    for elem in list:
        if(elem in elems_and_count):
            elems_and_count[elem] += 1
        else:
            elems_and_count[elem] = 1
    sorted_dict = dict(sorted(elems_and_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
    

def transform_dict_to_df(dict):
    """
    Transforms a dict into a df with two columns one for keys and the other for values

    Args:
        dict

    Returns:
        df
    """
    return pd.DataFrame(list(dict.items()), columns=['key', 'value'])

def remove_elem_from_list(list_elem_to_remove,full_list):
    """
    Removes specific elements from a list and returns a new list without them.

    Args:
        list_elem_to_remove (list): List of elements to be removed.
        full_list (list): Original list from which elements will be filtered out.

    Returns:
        list: A new list containing only the elements that are not in list_elem_to_remove.
    """
    list_elem_to_leave = []
    for elem in full_list:
        if elem not in list_elem_to_remove:
            list_elem_to_leave.append(elem)
    return list_elem_to_leave


