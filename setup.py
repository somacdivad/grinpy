from setuptools import setup, find_packages
import sys
import os

wd = os.path.dirname(os.path.abspath(__file__))
os.chdir(wd)
sys.path.insert(1, wd)

name = 'grinpy'
pkg = __import__('grinpy')

author, email = pkg.__author__.rsplit(' ', 1)
email = email.strip('<>')

version = pkg.__version__
classifiers = pkg.__classifiers__

readme = open(os.path.join(wd, 'README.rst'), 'r').readlines()
description = readme[1]
long_description = ''.join(readme)

reqs = [
        'networkx>=2.0',
        'coverage==4.0.3',
        ]

if sys.version_info < (2, 7):
    reqs.append('argparse')
    reqs.append('subprocess32')

setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    url='https://github.com/somacdivad/grinpy',
    maintainer=author,
    maintainer_email=email,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    install_requires=reqs,
    packages=find_packages(),
    license='Apache License 2.0',
    keywords='grinpy',
    entry_points={
        'console_scripts': [
            'coveralls = coveralls:wear',
        ],
    },
)
