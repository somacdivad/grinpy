# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functional interface for class methods."""

import grinpy as gp
from grinpy.functions.degree import degree_sequence

__all__ = ['is_graphic',
           'havel_hakimi_process',
           'elimination_sequence'
          ]

def is_graphic(lSequence):
    hh = gp.HavelHakimi(lSequence)
    return hh.is_graphic()

def havel_hakimi_process(nxGraph):
    return gp.HavelHakimi(degree_sequence(nxGraph))

def elimination_sequence(nxGraph):
    return havel_hakimi_process(nxGraph).get_elimination_sequence()
