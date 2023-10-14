## Local development instructions 

Install development dependencies: `pip install .`
Run tests if you want to verify code: `pytest`


### Upload to PyPI
1. Build package: `python setup.py sdist`
1. `pip install twine`
1. Optional: Install to test registry: 
   1. `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
   1. `pip install --index-url https://test.pypi.org/simple/ your-package-name`
1. `twine upload dist/*
`

### Incrementing package version

We should try to adhere to the [semantic versioning spec](https://semver.org/). In summary, semVer adheres to a MAJOR.MINOR.PATCH format. 

> Given a version number MAJOR.MINOR.PATCH, increment the: 
> MAJOR version when you make incompatible API changes
> MINOR version when you add functionality in a backward compatible manner
> PATCH version when you make backward compatible bug fixes
