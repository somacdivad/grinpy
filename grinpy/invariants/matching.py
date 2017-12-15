# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing matching related invariants for a graph."""

from grinpy import edges, is_matching, is_maximal_matching, number_of_edges
from itertools import combinations

__all__ = ['max_matching',
           'matching_number',
           'min_maximal_matching',
           'min_maximal_matching_number'
          ]

def max_matching(G):
    """Return a maximum matching in G.

    A *maximum matching* is a largest set of edges such that no two edges in
    the set have a common endpoint.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of edges in a maximum matching.
    """
    # return empty list if graph has no edges
    if number_of_edges(G) == 0: return []
    # loop through subsets of edges of G in decreasing order of size until a matching is found
    for i in reversed(range(1, number_of_edges(G) + 1)):
        for S in combinations(edges(G), i):
            if is_matching(G, set(S)):
                return list(S)

def matching_number(G):
    """Return the matching number of G.

    The *matching number* of a graph G is the cardinality of a maximum matching
    in G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The matching number of G.
    """
    return len(max_matching(G))

def min_maximal_matching(G):
    """Return a smallest maximal matching in G.

    A *maximal matching* is a maximal set of edges such that no two edges in
    the set have a common endpoint.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of edges in a smalles maximal matching.
    """
    # return empty list if graph has no edges
    if number_of_edges(G) == 0: return []
    # loop through subsets of edges of G in decreasing order of size until a matching is found
    for i in range(1, number_of_edges(G) + 1):
        for S in combinations(edges(G), i):
            if is_maximal_matching(G, set(S)):
                return list(S)

def min_maximal_matching_number(G):
    """Return the minimum maximal matching number of G.

    The *minimum maximal matching number* of a graph G is the cardinality of a
    smallest maximal matching in G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The minimum maximal matching number of G.
    """
    return len(min_maximal_matching(G))
