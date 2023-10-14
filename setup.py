from setuptools import setup, find_packages

setup(
    name='masdse203_rdb_to_semi',
    version='0.1.0',
    description='DSE 203 Relational to Semi Structured Transformation',
    author='Javier Garcia, Brian Qian',
    packages=find_packages(),
    install_requires=[
        "pytest>=7.1.1",
    ],
)

