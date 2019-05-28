# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Utility functions for dealing with combinations of things."""

import itertools
from grinpy import nodes


def pairs_of_nodes(G):
    return itertools.combinations(nodes(G), 2)
