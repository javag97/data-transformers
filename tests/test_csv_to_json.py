import pytest
from src.csv_to_json import csv_to_df

simple_data = {}

def test_simple_data_csv_df():
  assert csv_to_df(simple_data) == {}
