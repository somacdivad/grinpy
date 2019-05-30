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
__version__ = "19.30a1"

# import NetworkX dependency
import networkx  # noqa
from networkx import *  # noqa

import grinpy.classes  # noqa
from grinpy.classes import *  # noqa

import grinpy.functions  # noqa
from grinpy.functions import *  # noqa

import grinpy.invariants  # noqa
from grinpy.invariants import *  # noqa
