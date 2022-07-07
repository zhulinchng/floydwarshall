"""Script for setuptools."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

dependencies = [

]

setup(
    name='floydwarshall',
    version='1.0.0',
    author='Zhu Lin Ch\'ng',
    author_email='z.chng@liverpool.ac.uk',
    description='Floyd-Warshall algorithm for shortest path',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.csc.liv.ac.uk/sgzchng/floyd-warshall-algorithm',
    license='MIT',
    packages=find_packages(),
    install_requires=dependencies,
)
