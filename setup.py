from setuptools import setup, find_packages
import sys
import os

wd = os.path.dirname(os.path.abspath(__file__))
os.chdir(wd)
sys.path.insert(1, wd)

name = 'grinpy'
author = 'David Amos, Randy Davila'
email = 'amosd2@tamu.edu, davilar@uhd.edu'
version = '0.2.0a2'
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Software Development :: Libraries :: Python Modules',
]
copyright = "2017, %s " % author
license = """
   Copyright %s.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are
   met:

     * Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.

     * Redistributions in binary form must reproduce the above
       copyright notice, this list of conditions and the following
       disclaimer in the documentation and/or other materials provided
       with the distribution.

     * Neither the name of the NetworkX Developers nor the names of its
       contributors may be used to endorse or promote products derived
       from this software without specific prior written permission.

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
   OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
""" % copyright

readme = open(os.path.join(wd, 'README.md'), 'r').readlines()
description = readme[1]
long_description = ''.join(readme)

reqs = ['networkx>=2.0']

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

install_requires = ['networkx>=2.0']

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
