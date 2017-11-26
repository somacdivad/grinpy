# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing the residue and related invariants."""

from grinpy import havel_hakimi_process, elimination_sequence

__all__ = ['residue',
           'k_residue'
          ]

def residue(G):
    # TODO: Add documentation
    return havel_hakimi_process(G).residue()

def k_residue(G, k):
    # TODO: Add documentation
    elim_sequence = elimination_sequence(G)
    s = 0
    for i in range(k):
        s += (k - i) * elim_sequence.count(i)
    return s / k
