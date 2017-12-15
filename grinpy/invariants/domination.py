# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing dominating sets in a graph."""

from grinpy import is_connected, is_dominating_set, neighborhood, nodes, number_of_nodes, number_of_nodes_of_degree_k
from grinpy.invariants.dsi import sub_k_domination_number, sub_total_domination_number
from grinpy.invariants.independence import is_independent_set
from itertools import combinations

__all__ = ['is_k_dominating_set',
           'is_total_dominating_set',
           'is_connected_k_dominating_set',
           'is_connected_dominating_set',
           'min_k_dominating_set',
           'min_dominating_set',
           'min_total_dominating_set',
           'min_connected_k_dominating_set',
           'min_connected_dominating_set',
           'domination_number',
           'k_domination_number',
           'total_domination_number',
           'connected_k_domination_number',
           'connected_domination_number',
           'is_independent_k_dominating_set',
           'is_independent_dominating_set',
           'min_independent_k_dominating_set',
           'min_independent_dominating_set',
           'independent_k_domination_number',
           'independent_domination_number'
           ]

def is_k_dominating_set(G, nbunch, k):
    """Return whether or not the nodes in nbunch comprise a k-dominating set.

    A *k-dominating set* is a set of nodes with the property that every node in
    the graph is either in the set or adjacent at least 1 and at most k nodes
    in the set.

    This is a generalization of the well known concept of a dominating set
    (take k = 1).

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container or nodes.

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a k-dominating set, and False
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
    if k == 1:
        return is_dominating_set(G, nbunch)
    else:
        # exclude any nodes that aren't in G
        S = set(n for n in nbunch if n in G)
        # loop through the nodes in the complement of S and determine if they are adjacent to atleast k nodes in S
        others = set(nodes(G)).difference(S)
        for v in others:
            if len(set(neighborhood(G, v)).intersection(S)) < k:
                return False
        # if the above loop completes, nbunch is a k-dominating set
        return True

def is_total_dominating_set(G, nbunch):
    """Return whether or not the nodes in nbunch comprise a total dominating
    set.

    A * total dominating set* is a set of nodes with the property that every
    node in the graph is adjacent to some node in the set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container or nodes.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a k-dominating set, and False
        otherwise.
    """
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    # exclude any nodes that aren't in G
    S = set(n for n in nbunch if n in G)
    return set(neighborhood(G, nbunch)) == set(nodes(G))

def is_connected_k_dominating_set(G, nbunch, k):
    """ Return True if *nbunch* is a connected *k*-dominating set of *G*, and
    False otherwise.

    A set *D* is a *connected k-dominating set* of *G* is *D* is a
    *k*-dominating set in *G* and the subgraph of *G* induced by *D* is a
    connected graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container or nodes.

    k : int
        A positive integer

    Returns
    -------
    boolean
        True if *nbunch* is a connected *k*-dominating set in *G*, and false
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
    S = set(n for n in nbunch if n in G)
    H = G.subgraph(S)
    return is_k_dominating_set(G, S, k) and is_connected(H)

def is_connected_dominating_set(G, nbunch):
    """ Return True if *nbunch* is a connected dominating set of *G*, and
    False otherwise.

    A set *D* is a *connected dominating set* of *G* is *D* is a dominating
    set in *G* and the subgraph of *G* induced by *D* is a connected graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container or nodes.

    Returns
    -------
    boolean
        True if *nbunch* is a connected *k*-dominating set in *G*, and false
        otherwise.
    """
    return is_connected_k_dominating_set(G, nbunch, 1)

def min_k_dominating_set(G, k):
    """Return a smallest k-dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the sub-k-domination
    number of the graph, which was defined by Amos et al. and shown to be a
    tractable lower bound for the k-domination number.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    list
        A list of nodes in a smallest k-dominating set in the graph.

    References
    ----------
    D. Amos, J. Asplund, and R. Davila, The sub-k-domination number of a graph
    with applications to k-domination, *arXiv preprint arXiv:1611.02379*, (2016)
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    # use the sub-k-domination number to compute a starting point for the search range
    rangeMin = sub_k_domination_number(G, k)
    # loop through subsets of nodes of G in increasing order of size until a dominating set is found
    for i in range(rangeMin, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_k_dominating_set(G, S, k):
                return list(S)

def min_connected_k_dominating_set(G, k):
    """Return a smallest connected k-dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    list
        A list of nodes in a smallest k-dominating set in the graph.
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    # Only proceed with search if graph is connected
    if not is_connected(G): return None
    for i in range(0, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_connected_k_dominating_set(G, S, k):
                return list(S)

def min_connected_dominating_set(G, k):
    """Return a smallest connected dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest connected dominating set in the graph.
    """
    return min_connected_k_dominating_set(G, 1)

def min_dominating_set(G):
    """Return a smallest dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the sub-domination
    number of the graph, which was defined by Amos et al. and shown to be a
    tractable lower bound for the k-domination number.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    list
        A list of nodes in a smallest dominating set in the graph.

    See Also
    --------
    min_k_dominating_set

    References
    ----------
    D. Amos, J. Asplund, B. Brimkov and R. Davila, The sub-k-domination number
    of a graph with applications to k-domination, *arXiv preprint
    arXiv:1611.02379*, (2016)
    """
    return min_k_dominating_set(G, 1)

def min_total_dominating_set(G):
    """Return a smallest total dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the
    sub-total-domination number of the graph, which was defined by Davila and
    shown to be a tractable lower bound for the k-domination number.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest total dominating set in the graph.

    References
    ----------
    R. Davila, A note on sub-total domination in graphs. *arXiv preprint
    arXiv:1701.07811*, (2017)
    """
    # use naive lower bound for domination to compute a starting point for the search range
    rangeMin = sub_total_domination_number(G)
    # only process with search if graph has no isolated vertices
    if number_of_nodes_of_degree_k(G, 0) > 0: return None
    for i in range(rangeMin, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_total_dominating_set(G, S):
                return list(S)

def domination_number(G):
    """Return the domination number the graph.

    The *domination number* of a graph is the cardinality of a smallest
    dominating set of nodes in the graph.

    The method to compute this number modified brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The domination number of the graph.

    See Also
    --------
    min_dominating_set, k_domination_number
    """
    return len(min_dominating_set(G))

def k_domination_number(G, k):
    """Return the k-domination number the graph.

    The *k-domination number* of a graph is the cardinality of a smallest
    k-dominating set of nodes in the graph.

    The method to compute this number is modified brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The k-domination number of the graph.

    See Also
    --------
    min_k_dominating_set, domination_number
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    return len(min_k_dominating_set(G, k))

def connected_k_domination_number(G, k):
    """Return the connected k-domination number the graph.

    The *connected k-domination number* of a graph is the cardinality of a
    smallest k-dominating set of nodes in the graph that induces a connected
    subgraph.

    The method to compute this number is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The connected k-domination number of the graph.
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError('Expected k to be an integer.')
    k = int(k)
    if k < 1:
        raise ValueError('Expected k to be a positive integer.')
    D = min_connected_k_dominating_set(G, k)
    if D == None:
        return None
    else:
        return len(D)

def connected_domination_number(G):
    """Return the connected domination number the graph.

    The *connected domination number* of a graph is the cardinality of a
    smallest dominating set of nodes in the graph that induces a connected
    subgraph.

    The method to compute this number is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The connected domination number of the graph.
    """
    return connected_k_domination_number(G, 1)

def total_domination_number(G):
    """Return the total domination number the graph.

    The *total domination number* of a graph is the cardinality of a smallest
    total dominating set of nodes in the graph.

    The method to compute this number is modified brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The total domination number of the graph.
    """
    D = min_total_dominating_set(G)
    if D == None:
        return None
    else:
        return len(D)

def is_independent_k_dominating_set(G, nbunch, k):
    """ Return True if the nodes in nbunch comprise an independent k-dominating
    set in *G*, and return false otherwise.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container or nodes.

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise an independent k-dominating set,
        and False otherwise.
    """
    return is_k_dominating_set(G, nbunch, k) and is_independent_set(G, nbunch)

def is_independent_dominating_set(G, nbunch):
    """ Return True if the nodes in nbunch comprise an independent k-dominating
    set in *G*, and return false otherwise.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container or nodes.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise an independent dominating set, and
        False otherwise.
    """
    return is_k_dominating_set(G, nbunch, 1) and is_independent_set(G, nbunch)

def min_independent_k_dominating_set(G, k):
    """Return a smallest independent k-dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest independent k-dominating set in the graph.
    """
    # loop through subsets of nodes of G in increasing order of size until a total dominating set is found
    for i in range(1, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_independent_k_dominating_set(G, S, k):
                return list(S)

def min_independent_dominating_set(G):
    """Return a smallest independent dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest independent dominating set in the graph.
    """
    return min_independent_k_dominating_set(G, 1)

def independent_k_domination_number(G, k):
    """Return the independnet k-domination number the graph.

    The *independent k-domination number* of a graph is the cardinality of a
    smallest independent k-dominating set of nodes in the graph.

    The method to compute this number is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The independent k-domination number of the graph.
    """
    return len(min_independent_k_dominating_set(G, k))

def independent_domination_number(G):
    """Return the independnet domination number the graph.

    The *independent domination number* of a graph is the cardinality of a
    smallest independent dominating set of nodes in the graph.

    The method to compute this number is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The independent domination number of the graph.
    """
    return independent_k_domination_number(G, 1)
