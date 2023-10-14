from setuptools import setup, find_packages

setup(
    name='masdse203_rdb_to_semi',
    version='0.1.0',
    description='DSE 203 Relational to Semi Structured Transformation',
    author='Javier Garcia, Brian Qian',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        "pytest>=7.1.1",
        "bigtree>=0.13.0",
        "numpy<=1.26.1",
        "pandas<=2.1.1"
    ],
)

