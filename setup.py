from setuptools import setup, find_packages
import os

version = '0.0.0'
with open(os.path.join('pyheating', '__init__.py')) as fp:
    for line in fp:
        if line.strip().startswith('version ='):
            version = line.strip().split('=')[-1]


setup(
    name='pyheating',
    version=version,
    packages=find_packages(),
)