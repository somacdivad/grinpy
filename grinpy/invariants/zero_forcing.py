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
from grinpy import is_connected, min_degree, neighborhood, nodes, number_of_nodes

__all__ = ['is_k_forcing_vertex',
           'is_k_forcing_active_set',
           'is_k_forcing_set',
           'min_k_forcing_set',
           'k_forcing_number',
           'is_zero_forcing_vertex',
           'is_zero_forcing_active_set',
           'is_zero_forcing_set',
           'min_zero_forcing_set',
           'zero_forcing_number',
           'is_total_zero_forcing_set',
           'min_total_zero_forcing_set',
           'total_zero_forcing_number',
           'is_connected_k_forcing_set',
           'is_connected_zero_forcing_set',
           'min_connected_k_forcing_set',
           'min_connected_zero_forcing_set',
           'connected_k_forcing_number',
           'connected_zero_forcing_number'
           ]

def is_k_forcing_vertex(G, v, nbunch, k):
    """Return whether or not *v* can *k*-force relative to the set of nodes
    in nbunch.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    v : a single node in *G*

    nbunch: a single node or iterable container of nodes in *G*.

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if *v* can *k*-force relative to the nodes in nbunch. False
        otherwise.
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    S = set( n for n in nbunch if n in G)
    n = len(set(neighborhood(G, v)).difference(S))
    return v in S and n >= 1 and n <= k

def is_k_forcing_active_set(G, nbunch, k):
    """Return whether or not at least one node in nbunch can *k*-force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch: a single node or iterable container of nodes in *G*

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if at least one of the nodes in nbunch can *k*-force. False
        otherwise.
    """
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    S = set(n for n in nbunch if n in G)
    for v in S:
        if is_k_forcing_vertex(G, v, S, k):
            return True
    return False

def is_k_forcing_set(G, nbunch, k):
    """Return whether or not the nodes in nbunch comprise a *k*-forcing set in
    *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch: a single node or iterable container of nodes in *G*.

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a *k*-forcing set in *G*. False
        otherwise.
    """
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    Z = set(n for n in nbunch if n in G)
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
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    list
        A list of nodes in a smallest *k*-forcing set in *G*.
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
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    int
        The *k*-forcing number of *G*.
    """
    return len(min_k_forcing_set(G, k))

def is_zero_forcing_vertex(G, v, nbunch):
    """Return whether or not *v* can force relative to the set of nodes
    in nbunch.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    v: a single node in *G*

    nbunch: a single node or iterable container of nodes in *G*.

    Returns
    -------
    boolean
        True if *v* can force relative to the nodes in nbunch. False
        otherwise.
    """
    return is_k_forcing_vertex(G, v, nbunch, 1)

def is_zero_forcing_active_set(G, nbunch):
    """Return whether or not at least one node in nbunch can force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch: a single node or iterable container of nodes in *G*

    Returns
    -------
    boolean
        True if at least one of the nodes in nbunch can force. False
        otherwise.
    """
    return is_k_forcing_active_set(G, nbunch, 1)

def is_zero_forcing_set(G, S):
    """Return whether or not the nodes in nbunch comprise a zero forcing set in
    *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch: a single node or iterable container of nodes in *G*.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a zero forcing set in *G*. False
        otherwise.
    """
    return is_k_forcing_set(G, S, 1)

def min_zero_forcing_set(G):
    """Return a smallest zero forcing set in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest zero forcing set in *G*.
    """
    return min_k_forcing_set(G, 1)

def zero_forcing_number(G):
    """Return the zero forcing number of *G*.

    The zero forcing number of a graph is the cardinality of a smallest
    zero forcing set in the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The zero forcing number of *G*.
    """
    return len(min_zero_forcing_set(G))

def is_total_zero_forcing_set(G, nbunch):
    """Return whether or not the nodes in nbunch comprise a total zero forcing
    set in *G*.

    A *total zero forcing set* in a graph *G* is a zero forcing set that does
    not induce any isolated vertices.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch: a single node or iterable container of nodes in *G*.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a total zero forcing set in *G*.
        False otherwise.
    """
    try:
      _ = (v for v in nbunch)
    except:
      nbunch = [nbunch]
    S = set(n for n in nbunch if n in G)
    for v in S:
      if set(neighborhood(G, v)).intersection(S) == set():
        return False
    return is_zero_forcing_set(G, S)

def min_total_zero_forcing_set(G):
    """Return a smallest total zero forcing set in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest zero forcing set in *G*.
    """
    # loop through subsets of nodes of G in increasing order of size until a zero forcing set is found
    for i in range(2, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_total_zero_forcing_set(G, S):
                return list(S)
    # if the above loop completes, return None (should not occur)
    return None

def total_zero_forcing_number(G):
    """Return the total zero forcing number of *G*.

    The *total zero forcing number* of a graph is the cardinality of a smallest
    total zero forcing set in the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The total zero forcing number of *G*.
    """
    return len(min_total_zero_forcing_set(G))

def is_connected_k_forcing_set(G, nbunch, k):
    """Return whether or not the nodes in nbunch comprise a connected k-forcing
    set in *G*.

    A *connected k-forcing set* in a graph *G* is a k-forcing set that induces
    a connected subgraph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch: a single node or iterable container of nodes in *G*.

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a connected k-forcing set in *G*.
        False otherwise.
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    S = set(n for n in nbunch if n in G)
    H = G.subgraph(S)
    return is_k_forcing_set(G, S, k) and is_connected(H)

def is_connected_zero_forcing_set(G, nbunch):
    """Return whether or not the nodes in nbunch comprise a connected zero
    forcing set in *G*.

    A *connected zero forcing set* in a graph *G* is a zero forcing set that
    induces a connected subgraph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch: a single node or iterable container of nodes in *G*.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a connected zero forcing set in
        *G*. False otherwise.
    """
    return is_connected_k_forcing_set(G, nbunch, 1)

def min_connected_k_forcing_set(G, k):
    """Return a smallest connected k-forcing set in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer

    Returns
    -------
    list
        A list of nodes in a smallest connected k-forcing set in *G*.
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    # loop through subsets of nodes of G in increasing order of size until a zero forcing set is found
    for i in range(1, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_connected_k_forcing_set(G, S, k):
                return list(S)
    # if the above loop completes, return None (should not occur)
    return None

def min_connected_zero_forcing_set(G):
    """Return a smallest connected zero forcing set in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer

    Returns
    -------
    list
        A list of nodes in a smallest connected zero forcing set in *G*.
    """
    return min_connected_k_forcing_set(G, 1)

def connected_k_forcing_number(G, k):
    """Return the connected k-forcing number of *G*.

    The *connected k-forcing number* of a graph is the cardinality of a smallest
    connected k-forcing set in the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The connected k-forcing number of *G*.
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    return len(min_connected_k_forcing_set(G, k))

def connected_zero_forcing_number(G):
    """Return the connected zero forcing number of *G*.

    The *connected zero forcing number* of a graph is the cardinality of a
    smallest connected zero forcing set in the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The connected k-forcing number of *G*.
    """
    return connected_k_forcing_number(G, 1)
