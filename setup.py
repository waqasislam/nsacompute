#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='nsacompute',
      version='0.1.0',
      description='Learn math and do advanced computations for python.',
      author='Waqas Islam',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['nsacompute'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['numpy', 'sympy'],
      python_requires='>=3.8',
      include_package_data=True)
