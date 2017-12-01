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
    """Return whether or not the nodes in nbunch comprise a k-dominating set.

    A *k-dominating set* is a set of nodes with the property that every node in
    the graph is either in the set or adjacent at least 1 and at most k nodes
    in the set.

    This is a generalization of the well known concept of a dominating set
    (take k = 1).

    Parameters
    ----------
    G : graph
        A Networkx graph.

    nbunch: a single node or iterable container or nodes

    k : int
        A positive integer.

    Returns
    -------
    isKDominating : bool
        True if the nodes in nbunch comprise a k-dominating set, and False
        otherwise.
    """
    # TODO: add check that k >= 1 and throw error if not
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
    G : graph
        A Networkx graph.

    nbunch: a single node or iterable container or nodes

    Returns
    -------
    isTotalDominating : bool
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

def min_k_dominating_set(G, k):
    """Return a smallest k-dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the sub-k-domination
    number of the graph, which was defined by Amos et al. and shown to be a
    tractable lower bound for the k-domination number.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    k : int
        A positive integer.

    Returns
    -------
    minKDominatingSet : list
        A smallest k-dominating set in the graph.

    References
    ----------
    D. Amos, J. Asplund, and R. Davila, The sub-k-domination number of a graph
    with applications to k-domination, *arXiv preprint arXiv:1611.02379*, (2016)
    """
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
    """Return a smallest dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the sub-domination
    number of the graph, which was defined by Amos et al. and shown to be a
    tractable lower bound for the k-domination number.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    k : int
        A positive integer.

    Returns
    -------
    minDominatingSet : list
        A smallest dominating set in the graph.

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
    G : graph
        A Networkx graph.

    Returns
    -------
    minTotalDominatingSet : list
        A smallest total dominating set in the graph.

    References
    ----------
    R. Davila, A note on sub-total domination in graphs. *arXiv preprint
    arXiv:1701.07811*, (2017)
    """
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
    """Return the domination number the graph.

    The *domination number* of a graph is the cardinality of a smallest
    dominating set of nodes in the graph.

    The method to compute this number modified brute force.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    dominationNumber : int
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
    G : graph
        A Networkx graph.

    Returns
    -------
    kDominationNumber : int
        The k-domination number of the graph.

    See Also
    --------
    min_k_dominating_set, domination_number
    """
    return len(min_k_dominating_set(G, k))

def total_domination_number(G):
    """Return the total domination number the graph.

    The *total domination number* of a graph is the cardinality of a smallest
    total dominating set of nodes in the graph.

    The method to compute this number is modified brute force.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    totalDominationNumber : int
        The total domination number of the graph.
    """
    return len(min_total_dominating_set(G))
