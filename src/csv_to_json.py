"""Homework 1"""
import pandas as pd
import numpy as np
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
    
def valdiate_schema_csv(schema):
    """
    Validates the schema.csv file for its structure and content.

    Parameters:
        filepath (schema): A pandas dataframe representation of a schema

    Returns:
        bool: True if the CSV is valid, False otherwise.
    """


    expected_columns = [
        "conname", "conrelid", "conrelid_file", "fk_column",
        "confrelid_file", "confrelid", "pk_column"
    ]

    missing_columns = set(expected_columns) - set(schema.columns)
    extra_columns = set(schema.columns) - set(expected_columns)

    if missing_columns or extra_columns:
        error_message = ""
        if missing_columns:
            error_message += f"Missing values: {', '.join(missing_columns)}. "
        if extra_columns:
            error_message += f"Extra values: {', '.join(extra_columns)}"
        raise ValueError(error_message)

    if not set(schema['fk_column']).issubset(schema['pk_column']) or not set(schema['pk_column']).issubset(schema['fk_column']):
        raise ValueError("Mismatch between foreign key and primary key columns.")
    
    return True

def merge_df(df1, df2, db_schema):    
    df1_name = db_schema['conrelid'][0] # Name of the table with the foreign key constraint.

    fk_col = db_schema['fk_column'][0] # Foreign key column in the table with the constraint.
    pk_col = db_schema['pk_column'][0] # Primary key column in the referenced table.

    # Rename the column in df2 to match the fk_col in df1, if they're different.
    if fk_col != pk_col:
        df2 = df2.rename(columns={pk_col: fk_col})

    df1_columns = list(np.setdiff1d(df1.columns, [fk_col])) # Columns in df1 besides the foreign key.
    df2_columns = list(np.setdiff1d(df2.columns, [fk_col]))

    # If both dataframes have columns with the same name that's not the foreign key.
    dup_col_name = np.intersect1d(df2_columns, df1_columns)
    if len(dup_col_name) != 0:
        for col in dup_col_name:
            df1 = df1.rename({col: col+'_x'}, axis=1)
            df2 = df2.rename({col: col+'_y'}, axis=1)
            df1_columns = list(np.setdiff1d(df1.columns, [fk_col]))
            df2_columns = list(np.setdiff1d(df2.columns, [fk_col]))

    df = df1.merge(df2, on=fk_col)
    all_cols = [fk_col] + df2_columns 
    temp = (df.groupby(all_cols)[df1_columns]
            .apply(lambda x: x.to_dict('records'))
            .reset_index(name=df1_name)
            .to_json(orient='records')
            )
    parsed = json.loads(temp)


def df_to_json(*args, db_schema=None):
    """Converts one or multiple pandas DataFrames to JSON format.
    
    If a single dataframe is passed, it's converted to a JSON array of records.
    If multiple dataframes are passed, they are merged together according to the database schema.
    This works for two dataframes
    
    Parameters:
        *args: One or more pandas DataFrames to convert.
        db_schema (str): An optional parameter that could be used to customize the JSON structure based on SQL schema relationships.
    
    Returns:
        list: A list containing the JSON representation of each DataFrame.
    """
    for df in args:
        if not is_df(df):
            raise ValueError("One of your dataframes is not valid.")

    if len(args) == 1:
        if db_schema is not None:
            raise ValueError("No schema needed with one table.")
        results = args[0].to_json(orient='records')
        parsed = json.loads(results)
        return parsed
        
    if db_schema is None:
        raise ValueError("Expected a db_schema, but received None.")

    if not valdiate_schema_csv(db_schema):
        return
        # raise ValueError("Your schema is not valid.")
    
    if len(args) == 2:
        parsed = merge_df(args[0], args[1], db_schema)
        print(parsed)
        df2_name = db_schema['confrelid'][0] # Name of the referenced table.
        final = json.dumps({df2_name: parsed})
        print(final)
        with open("results.json", "w") as outfile: #fix: write out to results folder
            outfile.write(final)
        return parsed
        
