# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gradient',
    version='0.1.0',
    description='Sample client for GradeCam Gradient',
    long_description=readme,
    author='GradeCam Development',
    author_email='support@gradecam.com',
    url='https://github.com/gradecam/python-gradient-client',
    license=license,
    packages=find_packages(exclude=('tests'))
)
