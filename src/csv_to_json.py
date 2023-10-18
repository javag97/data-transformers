"""Homework 1"""
import pandas as pd
import json


def is_df(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Expected a DataFrame, but received a different type.")
        return False
    else:
        return True
    

def df_to_json(*args, db_schema=None):
    """Assumes database has been loaded into a df, then transforms into a JSON file."""

    if len(args) == 1:
        if is_df(args[0]):
            results = args[0].to_json(orient='records')
            parsed = json.loads(results)
            return parsed
    
    if db_schema == None:
        raise ValueError("Expected a db_schema, but received None.")

    data = []

    for df in args:
        if is_df(df):
            return None
        results = df.to_json(orient='records')
        parsed = json.loads(results)
        data.append(parsed)
    
    return data
  