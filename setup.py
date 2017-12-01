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

readme = open(os.path.join(wd, 'README.md'), 'r').readlines()
description = readme[1]
long_description = ''.join(readme)

reqs = [
        'networkx>=2.0',
        ]

if sys.version_info < (2, 7):
    reqs.append('argparse')
    reqs.append('subprocess32')

if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'coverage'
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirments." % err_msg
        raise ImportError(msg)
    os.system('py.test --cov-config .coveragerc --cov=grinpy')
    sys.exit()

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
    license='BSD',
    keywords='grinpy',
    entry_points={
        'console_scripts': [
            'coveralls = coveralls:wear',
        ],
    },
)
