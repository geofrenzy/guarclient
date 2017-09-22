# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="uasclient",
    version="0.1.0",
    description="A client for querying the Global Unmanned Airframe Registry",
    license="MIT",
    author="GeoNetwork",
    packages=find_packages(),
    install_requires=[
        "dnspython"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
