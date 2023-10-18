"""Homework 1"""
import pandas as pd
import json


def is_df(df):
    """Check if the input is a pandas DataFrame.
    
    Parameters:
        df: The object to check.
    
    Returns:
        bool: True if df is a pandas DataFrame, otherwise raises a ValueError.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Expected a DataFrame, but received a different type.")
    else:
        return True
    

def df_to_json(*args, db_schema=None):
    """Converts one or multiple pandas DataFrames to JSON format.
    
    If a single dataframe is passed, it's converted to a JSON array of records.
    If multiple dataframes are passed, they are merged together according to the database schema.
    This is not done yet.
    
    Parameters:
        *args: One or more pandas DataFrames to convert.
        db_schema (str): An optional parameter that could be used to customize the JSON structure based on SQL schema relationships.
    
    Returns:
        list: A list containing the JSON representation of each DataFrame.
    """
    if len(args) == 1:
        if is_df(args[0]):
            results = args[0].to_json(orient='records')
            parsed = json.loads(results)
            return parsed
    
    if db_schema == None:
        raise ValueError("Expected a db_schema, but received None.")

    data = []

    for df in args:
        if not is_df(df):
            raise ValueError("One of your dataframes is not valid.")
        # todo: Implement merging logic based on db_schema
    
    return data
  