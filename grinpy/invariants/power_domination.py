# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing power domination related invariants of a graph."""

from grinpy import closed_neighborhood, nodes, number_of_nodes
from grinpy.invariants.zero_forcing import is_zero_forcing_set, is_k_forcing_set
from itertools import combinations

__all__ = ['is_power_dominating_set',
           'min_power_dominating_set',
           'power_domination_number',
           'is_k_power_dominating_set',
           'min_k_power_dominating_set',
           'k_power_domination_number'
           ]

def is_k_power_dominating_set(G, nbunch, k):
    """Return whether or not the nodes in nbunch comprise a k-power dominating
    set.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    nbunch : a single node or iterable container of nodes.

    Returns
    -------
    isPowerDominating : bool
        True if the nodes in nbunch comprise a power dominating set, False
        otherwise.
    """
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    return is_k_forcing_set(G, closed_neighborhood(G, nbunch), k)

def min_k_power_dominating_set(G, k):
    """Return a smallest k-power dominating set of nodes in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    minkPowerDominatingSet : list
        A smallest power dominating set in *G*.
    """
    for i in range(1, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_k_power_dominating_set(G, S,k):
                return list(S)
    # if above loop completes, return None (should not occur)
    return None

def k_power_domination_number(G, k):
    """Return the k-power domination number of *G*.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    kpowerDominationNumber : int
        The k-power domination number of *G*.
    """
    return len(min_k_power_dominating_set(G, k))

""" The following functions compute the special cases of k-power domination when k = 1 """

def is_power_dominating_set(G, nbunch):
    return is_k_power_dominating_set(G, nbunch, 1)

def min_power_dominating_set(G):
    return min_k-power_dominating_set(G,1)

def power_domination_number(G):
    return k_power_domination_number(G,1)
