import pytest
from src.csv_to_json import df_to_json
import pandas as pd
import json


@pytest.fixture
def one_table():
    df = pd.read_csv('tests/data/one_table/table.csv')
    return df

@pytest.fixture
def one_table_result():
    with open('tests/data/one_table/result.json', 'r') as json_file:
        data = json.load(json_file)
    return data

def test_invalid_input():
    with pytest.raises(ValueError):
        df_to_json('string')

def test_simple_data_csv_df(one_table, one_table_result):
    assert df_to_json(one_table) == one_table_result

@pytest.fixture
def two_tables():
    df1 = pd.read_csv('tests/data/two_tables/df_topic.csv')
    df2 = pd.read_csv("tests/data/two_tables/df_doc.csv")
    return df1, df2

def test_one_table_with_schema(two_tables):
    df1, df2 = two_tables
    schema = pd.read_csv('tests/data/two_tables/schema.csv')
    with pytest.raises(ValueError):
        df_to_json(df1, db_schema = schema)

def test_two_tables_no_schema(two_tables):
    df1, df2 = two_tables
    with pytest.raises(ValueError):
        df_to_json(df1, df2)

def test_two_tables(two_tables):
    df1, df2 = two_tables
    schema = pd.read_csv('tests/data/two_tables/schema.csv')
    end = df_to_json(df1, df2, db_schema = schema)
    return end

@pytest.fixture
def two_tables_result():
    with open('tests/data/two_tables/results.json', 'r') as json_file:
        data = json.load(json_file)
    return data

def test_simple_data_csv_df(two_tables, two_tables_result):
    schema = pd.read_csv('tests/data/two_tables/schema.csv')
    df1, df2 = two_tables
    result = json.loads(df_to_json(df1, df2, db_schema=schema))
    assert two_tables_result == two_tables_result
