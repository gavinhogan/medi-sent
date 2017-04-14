"""
The setup module for the MediSent hospital sentiment analylzer
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path, environ
import subprocess

try:
    version = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').rstrip()
except:
    version = '0.0.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='medi-sent',
    version=version,

    description='Analyze Twitter to Determine Public Sentiment for Hospitals',
    long_description=long_description,

    url='https://github.com/gavinhogan/medi-sent.git',
    author='Gavin Hogan',

    packages=find_packages(),

    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'tweepy==3.5.0',
        'textblob==0.12.0'
    ],

    entry_points={
        'console_scripts': [
            'medi-sent=medi-sent.__main__:main'
        ]
    }
)