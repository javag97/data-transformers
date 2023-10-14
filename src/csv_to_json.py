"""Working with CSV files using pandas."""
import pandas
import json

def csv_to_json(csv):
  """Assumes database has been loaded into a CSV, then transforms into a python dictionary."""
  df = pandas.read_csv(csv)
  results = df.to_json(orient='records')
  parsed = json.loads(results)
  return parsed
  