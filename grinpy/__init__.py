# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>

"""Top-level package for GrinPy."""

# check Python version
import sys

if sys.version_info[:2] < (3, 4):
    m = "Python 3.4 or later is required for GrinPy (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

__author__ = """David Amos, Randy Davila"""
__email__ = "somacdivad@gmail.com, davilar@uhd.edu"
__version__ = "19.30a0"

# import NetworkX dependency
import networkx  # noqa
from networkx import *  # noqa

from .classes import *  # noqa

from .functions import *  # noqa

from .invariants import *  # noqa
