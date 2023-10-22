import pytest
from src.csv.to_json import df_to_json
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

def test_two_tables_no_schema(two_tables):
    df1, df2 = two_tables
    with pytest.raises(ValueError):
        df_to_json(df1, df2)

@pytest.fixture
def two_tables_schema():
    schema = pd.read_csv('tests/data/two_tables/schema.csv')
    return schema

def test_two_tables_bad_schema(two_tables):
    df1, df2 = two_tables
    schema = pd.read_csv('tests/data/two_tables/bad_schema.csv')
    with pytest.raises(ValueError):
        df_to_json(df1, df2, db_schema = schema)

def test_two_tables_incomplete_schema(two_tables):
    df1, df2 = two_tables
    schema = pd.read_csv('tests/data/two_tables/incomplete_schema.csv')
    with pytest.raises(ValueError):
        df_to_json(df1, df2, db_schema = schema)

def test_one_table_with_schema(two_tables, two_tables_schema):
    df1, df2 = two_tables
    with pytest.raises(ValueError):
        df_to_json(df1, db_schema = two_tables_schema)

@pytest.fixture
def two_tables_result():
    with open('tests/data/two_tables/results.json', 'r') as json_file:
        data = json.load(json_file)
    return data

def test_simple_data_csv_df(two_tables, two_tables_schema, two_tables_result):
    df1, df2 = two_tables
    result = json.loads(df_to_json(df1, df2, db_schema=two_tables_schema))
    assert result == two_tables_result

@pytest.fixture
def multiple_relations():
    df1 = pd.read_csv('tests/data/two_tables_multiple_relations/courses.csv')
    df2 = pd.read_csv("tests/data/two_tables_multiple_relations/students.csv")
    return df1, df2

@pytest.fixture
def multiple_relations_result():
    with open('tests/data/two_tables_multiple_relations/results.json', 'r') as json_file:
        data = json.load(json_file)
    return data

@pytest.fixture
def multiple_relations_schema():
    schema = pd.read_csv('tests/data/two_tables_multiple_relations/schema.csv')
    return schema

def test_two_tables_multiple_relations(multiple_relations, multiple_relations_schema, multiple_relations_result):
    df1, df2 = multiple_relations
    result = json.loads(df_to_json(df1, df2, db_schema=multiple_relations_schema))
    assert result == multiple_relations_result
