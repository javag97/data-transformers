"""Homework 1"""
import pandas as pd
import json

def df_to_json(df):
    """Assumes database has been loaded into a df, then transforms into a JSON file."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Expected a DataFrame, but received a different type.")
    
    print(df.dtypes)

    results = df.to_json(orient='records')
    parsed = json.loads(results)
    return parsed
  