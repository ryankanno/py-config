#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import py_config

packages = [
    'py_config',
    'py_config.backends',
]

requires = ['pyyaml']
tests_require = ['flake8', 'mock', 'nose', 'nosexcover']

with open('README.rst') as f:
    readme = f.read()

with open('CHANGES') as f:
    changes = f.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
    'Topic :: Utilities'
]

setup(
    name='py-config',
    version=py_config.__version__,
    description='Tiny configuration wrapper module',
    long_description=readme + '\n\n' + changes,
    author='Ryan Kanno',
    author_email='ryankanno@localkinegrinds.com',
    url="https://github.com/ryankanno/py-config",
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'py_config': 'py_config'},
    install_requires=requires,
    license='MIT',
    tests_require=tests_require,
    classifiers=classifiers,
)

# vim: filetype=python
