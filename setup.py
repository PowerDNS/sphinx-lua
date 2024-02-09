#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    import setuptools_git
except ImportError:
    print("WARNING!")
    print("We need the setuptools-git package to be installed for")
    print("some of the setup.py targets to work correctly.")

PACKAGE = 'sphinx-lua'

setup(
    name = PACKAGE,
    version = '0.1.1', # latest repository tag. manually set
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    namespace_packages = ['redjack', 'redjack.sphinx'],
    install_requires = ['Sphinx'],
)
