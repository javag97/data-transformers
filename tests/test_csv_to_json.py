import pytest
from src.csv_to_json import csv_to_df

@pytest.fixture
def sample_dict():
    return {"Python": 3}

def test_simple_data_csv_df(sample_dict):
  assert csv_to_df(sample_dict) == {'Python': 3}
