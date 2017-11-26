# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing dominating sets in a graph."""

from grinpy import is_dominating_set, neighborhood, nodes, number_of_nodes
from grinpy.invariants.dsi import sub_k_domination_number, sub_total_domination_number
from itertools import combinations


__all__ = ['is_k_dominating_set',
           'is_total_dominating_set',
           'min_k_dominating_set',
           'min_dominating_set',
           'min_total_dominating_set',
           'domination_number',
           'k_domination_number',
           'total_domination_number'
           ]

def is_k_dominating_set(G, nbunch, k):
    # TODO: Add documentation
    # TODO: add check that k >= 1 and throw error if not
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    if k == 1:
        return is_dominating_set(G, nbunch)
    else:
        S = set(nbunch)
        # loop through the nodes in the complement of S and determine if they are adjacent to atleast k nodes in S
        others = set(nodes(G)).difference(S)
        for v in others:
            if len(set(neighborhood(G, v)).intersection(S)) < k:
                return False
        # if the above loop completes, nbunch is a k-dominating set
        return True

def is_total_dominating_set(G, nbunch):
    # TODO: Add documentation
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    return set(neighborhood(G, nbunch)) == set(nodes(G))

def min_k_dominating_set(G, k):
    # TODO: Add documentation
    # use the sub-k-domination number to compute a starting point for the search range
    rangeMin = sub_k_domination_number(G, k)
    # loop through subsets of nodes of G in increasing order of size until a dominating set is found
    for i in range(rangeMin, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_k_dominating_set(G, S, k):
                return list(S)
    # return None if no dominating set is found (should not occur)
    return None

def min_dominating_set(G):
    # TODO: Add documentation
    return min_k_dominating_set(G, 1)

def min_total_dominating_set(G):
    # TODO: Add documentation
    # use naive lower bound for domination to compute a starting point for the search range
    rangeMin = sub_total_domination_number(G)
    # loop through subsets of nodes of G in increasing order of size until a total dominating set is found
    for i in range(rangeMin, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_total_dominating_set(G, S):
                return list(S)
    # return None if no total dominating set is found (should not occur)
    return None

def domination_number(G):
    # TODO: Add documentation
    return len(min_dominating_set(G))

def k_domination_number(G, k):
    # TODO: Add documentation
    return len(min_k_dominating_set(G, k))

def total_domination_number(G):
    # TODO: Add documentation
    return len(min_total_dominating_set(G))
