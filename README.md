# This project is currently in development and is not considered stable. 

URL to package: https://test.pypi.org/project/masdse203-rdb-to-semi/

##  Basic Usage 
1. Install the rdb-to-semi PyPi package
```bash
pip install -i https://test.pypi.org/simple/ masdse203-rdb-to-semi
```
2. Import df_to_json
```python
from masdse203_rdb_to_semi.to_json import df_to_json
```
3. Different use cases:
- If you have one dataframe to convert
```python
df1 = pd.read_csv('path_to.csv')
df_to_json(df1)
```
- If you have two dataframes to convert include a schema csv
```python
df1 = pd.read_csv('path_to.csv')
df2 = pd.read_csv("path_to_other.csv")
schema = pd.read_csv('schema.csv') 
df_to_json(df1, df2, db_schema=schema)
```

## Defining the schema object

If you're merging two tables together, you need to offer a schema in the form of the CSV to understand the primary/foreign key relationships between tables. This is **required**, *must* be user generated, and these tables **will not be merged without it.**

### Creating the schema CSV 

| conname       | conrelid | fk_column   | confrelid | pk_column   |
|---------------|----------|-------------|-----------|-------------|
| topics_fk_doc | topics   | document_id | documents | document_id |

- conname: the name of the constraint (you can name this anything)
- conrelid:  the name of the table the constraint is on
- fk_column: the column of the foreign key in conrelid
- confrelid: the name of the table being referenced 
- pk_column: the column of the primary key in confrelid that is being referenced

## Local development instructions 

* Install development dependencies: `pip install .`
* Run tests if you want to verify code: `pytest`

The empty `__init.py` files are to treat that directory as a module, thus allowing it to be imported using the import statement in Python scripts.

```
## within the test directory
from src.csv_to_json import csv_to_df
```

### Upload to PyPI
1. Build package: `python setup.py sdist`
1. `pip install twine`
1. Optional: Upload to test registry and import test package: 
   1. Upload to test registry: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
   1. To test the package: `pip install --index-url https://test.pypi.org/simple/ masdse203-rdb-to-semi`
2. `twine upload dist/*` for push to directory

### Incrementing package version

We should try to adhere to the [semantic versioning spec](https://semver.org/). In summary, semVer adheres to a MAJOR.MINOR.PATCH format. 

> Given a version number MAJOR.MINOR.PATCH, increment the: 
> MAJOR version when you make incompatible API changes
> MINOR version when you add functionality in a backward compatible manner
> PATCH version when you make backward compatible bug fixes

