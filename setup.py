from setuptools import setup, find_packages

setup(
    name='masdse203_rdb_to_semi',
    version='0.1.3.alpha',
    description='DSE 203 Relational to Semi Structured Transformation',
    author='Javier Garcia, Brian Qian',
    author_email='jag043@ucsd.edu',
    url='https://github.com/javag97/data-transformers/',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires='>=3.8',
    install_requires=[
        "pytest>=7.1.1",
        "numpy<=1.26.1",
        "pandas<=2.1.1"
    ],
)
