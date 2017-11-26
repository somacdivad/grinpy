# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing zero forcing related invariants of a graph."""

from itertools import combinations
from grinpy import min_degree, neighborhood, nodes, number_of_nodes

__all__ = ['is_k_forcing_vertex',
           'is_k_forcing_active_set',
           'is_k_forcing_set',
           'min_k_forcing_set',
           'k_forcing_number',
           'is_zero_forcing_vertex',
           'is_zero_forcing_active_set',
           'is_zero_forcing_set',
           'min_zero_forcing_set',
           'zero_forcing_number'
           ]

def is_k_forcing_vertex(G, v, nbunch, k):
    # TODO: Add documentation
    # TODO: add check that k >= 1
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    S = set(nbunch)
    n = len(set(neighborhood(G, v)).difference(S))
    return v in S and n >= 1 and n <= k

def is_k_forcing_active_set(G, nbunch, k):
    # TODO: Add documentation
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    S = set(nbunch)
    for v in S:
        if is_k_forcing_vertex(G, v, S, k):
            return True
    return False

def is_k_forcing_set(G, nbunch, k):
    # TODO: Add documentation
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    Z = set(nbunch)
    while is_k_forcing_active_set(G, Z, k):
        Z_temp = Z.copy()
        for v in Z:
            if is_k_forcing_vertex(G, v, Z, k):
                Z_temp |= set(neighborhood(G, v))
        Z = Z_temp
    return Z == set(nodes(G))

def min_k_forcing_set(G, k):
    # TODO: Add documentation
    # use naive lower bound to compute a starting point for the search range
    rangeMin = min_degree(G) if k == 1 else 1
    # loop through subsets of nodes of G in increasing order of size until a zero forcing set is found
    for i in range(rangeMin, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_k_forcing_set(G, S, k):
                return list(S)
    # if the above loop completes, return None (should not occur)
    return None

def k_forcing_number(G, k):
    # TODO: Add documentation
    return len(min_k_forcing_set(G, k))

def is_zero_forcing_vertex(G, vertex, S):
    # TODO: Add documentation
    return is_k_forcing_vertex(G, vertex, S, 1)

def is_zero_forcing_active_set(G, S):
    # TODO: Add documentation
    return is_k_forcing_active_set(G, S, 1)

def is_zero_forcing_set(G, S):
    # TODO: Add documentation
    return is_k_forcing_set(G, S, 1)

def min_zero_forcing_set(G):
    # TODO: Add documentation
    return min_k_forcing_set(G, 1)

def zero_forcing_number(G):
    # TODO: Add documentation
    return len(min_zero_forcing_set(G))
