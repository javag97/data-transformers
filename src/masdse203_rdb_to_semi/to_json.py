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
    return True


def validate_schema_csv(schema):
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
    return True


def df_to_json(*args, db_schema=None):
    """Converts one or multiple pandas DataFrames to JSON format.
    
    If a single dataframe is passed, it's converted to a JSON array of records.
    If multiple dataframes are passed, they are merged together according to the database schema.
    This is not done yet.
    
    Parameters:
        *args: One or more pandas DataFrames to convert.
        db_schema (str): A parameter that could be used to customize the JSON structure based on SQL schema relationships. Not necessary for one table, but necessary for more. 
    
    Returns:
        list: A list containing the JSON representation of each DataFrame.
    """
    for df in args:
        if not is_df(df):
            raise ValueError("Expected dataframe, received something else.")

    if len(args) == 1:
        if db_schema is not None:
            raise ValueError("No schema needed with one table.")
        results = args[0].to_json(orient='records')
        parsed = json.loads(results)
        return parsed
    
    if db_schema is None:
        raise ValueError("Expected a db_schema, but received None.")
    
    if not validate_schema_csv(db_schema):
        return
    
    if len(args) == 2:
        df1, df2 = args
        schema_rows_len = db_schema.shape[0]
        for i in range(schema_rows_len):
            df1_name = db_schema['conrelid'][i] #name of table the constraint is on, foreign key
            shared_column = db_schema['fk_column'][i] #name of the foreign key in one table

            df1_columns = list(np.setdiff1d(df1.columns, [shared_column])) #columns in table besides shared column
            df2_columns = list(np.setdiff1d(df2.columns, [shared_column]))

            dup_col_name = np.intersect1d(df2_columns, df1_columns) #if both dataframes have columns with the same name that's not a foreign key
            if len(dup_col_name) != 0:
                for col in dup_col_name:
                    df1 = df1.rename({col: col+'_x'}, axis=1) #renaming both columns
                    df2 = df2.rename({col: col+'_y'}, axis=1)
                    df1_columns = list(np.setdiff1d(df1.columns, [shared_column])) 
                    df2_columns = list(np.setdiff1d(df2.columns, [shared_column]))

            df1 = df1.merge(df2, on=shared_column)

        all_cols = [shared_column] + df2_columns 
        temp = (df1.groupby(all_cols)[df1_columns]
                .apply(lambda x: x.to_dict('records'))
                .reset_index(name = df1_name)
                .to_json(orient='records')
                )
        parsed = json.loads(temp)

        return parsed
        
        # with open("results.json", "w", encoding='utf-8') as outfile: #fix: write out to results folder
        #     outfile.write(final)
        # return final
    
    return None
 