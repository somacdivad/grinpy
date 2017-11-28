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
    """Return whether or not *v* can *k*-force relative to the set of nodes
    in nbunch.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    v: a single node in *G*

    nbunch: a single node or iterable container of nodes in *G*.

    k : int
        A positive integer.

    Returns
    -------
    isForcing : bool
        True if *v* can *k*-force relative to the nodes in nbunch. False
        otherwise.
    """
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
    """Return whether or not at least one node in nbunch can *k*-force.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    nbunch: a single node or iterable container of nodes in *G*

    k : int
        A positive integer.

    Returns
    -------
    isActive : bool
        True if at least one of the nodes in nbunch can *k*-force. False
        otherwise.
    """
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
    """Return whether or not the nodes in nbunch comprise a *k*-forcing set in
    *G*.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    nbunch: a single node or iterable container of nodes in *G*.

    k : int
        A positive integer.

    Returns
    -------
    isForcingSet : bool
        True if the nodes in nbunch comprise a *k*-forcing set in *G*. False
        otherwise.
    """
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
    """Return a smallest *k*-forcing set in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    k : int
        A positive integer.

    Returns
    -------
    minForcingSet : list
        A smallest *k*-forcing set in *G*.
    """
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
    """Return the *k*-forcing number of *G*.

    The *k*-forcing number of a graph is the cardinality of a smallest
    *k*-forcing set in the graph.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    k : int
        A positive integer.

    Returns
    -------
    kForcingNum : int
        The *k*-forcing number of *G*.
    """
    return len(min_k_forcing_set(G, k))

def is_zero_forcing_vertex(G, v, nbunch):
    """Return whether or not *v* can force relative to the set of nodes
    in nbunch.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    v: a single node in *G*

    nbunch: a single node or iterable container of nodes in *G*.

    Returns
    -------
    isForcing : bool
        True if *v* can force relative to the nodes in nbunch. False
        otherwise.
    """
    return is_k_forcing_vertex(G, v, nbunch, 1)

def is_zero_forcing_active_set(G, nbunch):
    """Return whether or not at least one node in nbunch can force.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    nbunch: a single node or iterable container of nodes in *G*

    Returns
    -------
    isActive : bool
        True if at least one of the nodes in nbunch can force. False
        otherwise.
    """
    return is_k_forcing_active_set(G, nbunch, 1)

def is_zero_forcing_set(G, S):
    """Return whether or not the nodes in nbunch comprise a zero forcing set in
    *G*.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    nbunch: a single node or iterable container of nodes in *G*.

    Returns
    -------
    isForcingSet : bool
        True if the nodes in nbunch comprise a zero forcing set in *G*. False
        otherwise.
    """
    return is_k_forcing_set(G, S, 1)

def min_zero_forcing_set(G):
    """Return a smallest zero forcing set in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    minForcingSet : list
        A smallest zero forcing set in *G*.
    """
    return min_k_forcing_set(G, 1)

def zero_forcing_number(G):
    """Return the zero forcing number of *G*.

    The zero forcing number of a graph is the cardinality of a smallest
    zero forcing set in the graph.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    zeroForcingNum : int
        The zero forcing number of *G*.
    """
    return len(min_zero_forcing_set(G))
