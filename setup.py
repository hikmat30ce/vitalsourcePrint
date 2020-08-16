import setuptools
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="printbook",
    version="1.1.0",
    scripts=['printbook'],
    author="Hikmat Ullah",
    author_email="me@hikmatu.com",
    description="This tool download vital source book to images",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests', 'click', 'configparser'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],



)