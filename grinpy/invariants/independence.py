# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing independence related invariants for a graph."""

# imports
from itertools import combinations
from grinpy import neighborhood, nodes, number_of_edges, number_of_nodes
from grinpy.invariants.dsi import annihilation_number


__all__ = ['is_independent_set',
           'is_k_independent_set',
           'max_k_independent_set',
           'max_independent_set',
           'independence_number',
           'k_independence_number'
           ]

# methods
def is_independent_set(G, nbunch):
    # TODO: Add documentation
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    S = set(nbunch)
    return set(neighborhood(G, S)).intersection(S) == set()

def is_k_independent_set(G, nbunch, k):
    # TODO: Add documentation
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    if k == 1:
        return is_independent_set(G, nbunch)
    else:
        for v in nbunch:
            N = set(neighborhood(G, v))
            if len(N.intersection(nbunch)) >= k:
                return False
        return True

def max_k_independent_set(G, k):
    # TODO: Add documentation
    # set the maximum for the loop range
    rangeMax = number_of_nodes(G) + 1
    if k == 1:
        rangeMax = annihilation_number(G) + 1
    elif number_of_edges(G) > 0:
        rangeMax = number_of_nodes(G)
    # TODO: can the above range be improved with some general upper bound for the k-independence number?
    # loop through subsets of nodes of G in decreasing order of size until a k-independent set is found
    for i in reversed(range(rangeMax)):
        for S in combinations(nodes(G), i):
            if is_k_independent_set(G, S, k):
                return list(S)
    # return None if no independent set is found (should not occur)
    return None

def max_independent_set(G):
    # TODO: Add documentation
    return max_k_independent_set(G, 1)

def independence_number(G):
    # TODO: Add documentation
    return len(max_independent_set(G))

def k_independence_number(G, k):
    # TODO: Add documentation
    return len(max_k_independent_set(G, k))
