import pytest
from src.csv_to_json import df_to_json
import pandas as pd
import json


@pytest.fixture
def one_table():
    df = pd.read_csv('C:/Users/brian/Documents/data-transformers/tests/data/one_table/table.csv')
    return df

@pytest.fixture
def one_table_result():
    with open('C:/Users/brian/Documents/data-transformers/tests/data/one_table/result.json', 'r') as json_file:
        data = json.load(json_file)
    return data

def test_invalid_input():
    with pytest.raises(ValueError):
        df_to_json('string')

def test_simple_data_csv_df(one_table, one_table_result):
    assert df_to_json(one_table) == one_table_result

@pytest.fixture
def two_tables():
    df1 = pd.read_csv('C:/Users/brian/Documents/data-transformers/tests/data/two_tables/df_topic.csv')
    df2 = pd.read_csv("C:/Users/brian/Documents/data-transformers/tests/data/two_tables/df_doc.csv")
    return df1, df2

def test_two_tables(two_tables)::
    df1, df2 = two_tables
    schema = pd.read_csv('C:/Users/brian/Documents/data-transformers/tests/data/two_tables/schema.csv')
    #with pytest.raises(ValueError):
    end = df_to_json(df1, df2, db_schema = schema)
    return end


