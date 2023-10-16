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

def test_simple_data_csv_df(one_table, one_table_result):
    assert df_to_json(one_table) == one_table_result
