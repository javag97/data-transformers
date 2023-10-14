# This project is currently in active development and is not considered stable. 

## Local development instructions 

* Install development dependencies: `pip install .`
* Run tests if you want to verify code: `pytest`

The empty `__init.py` files are to treat that directory as a module, thus allowing it to be imported using the import statement in Python scripts.

```
## within the project
from src.csv_to_json import csv_to_df
```

### Upload to PyPI
1. Build package: `python setup.py sdist`
1. `pip install twine`
1. Optional: Upload to test registry and import test package: 
   1. Upload to test registry: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
   1. To test the package: `pip install --index-url https://test.pypi.org/simple/ your-package-name`
1. `twine upload dist/*
`

### Incrementing package version

We should try to adhere to the [semantic versioning spec](https://semver.org/). In summary, semVer adheres to a MAJOR.MINOR.PATCH format. 

> Given a version number MAJOR.MINOR.PATCH, increment the: 
> MAJOR version when you make incompatible API changes
> MINOR version when you add functionality in a backward compatible manner
> PATCH version when you make backward compatible bug fixes
