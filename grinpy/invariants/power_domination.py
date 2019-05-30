# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing power domination related invariants of a graph."""

from grinpy import set_closed_neighborhood
from grinpy.invariants.zero_forcing import is_k_forcing_set
from itertools import combinations

__all__ = [
    "is_k_power_dominating_set",
    "min_k_power_dominating_set",
    "k_power_domination_number",
    "is_power_dominating_set",
    "min_power_dominating_set",
    "power_domination_number",
]


def is_k_power_dominating_set(G, nodes, k):
    """Return whether or not the nodes in `nodes` comprise a k-power dominating
    set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if the nodes in `nodes` comprise a k-power dominating set, False
        otherwise.
    """
    return is_k_forcing_set(G, set_closed_neighborhood(G, nodes), k)


def min_k_power_dominating_set(G, k):
    """Return a smallest k-power dominating set of nodes in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest k-power dominating set in *G*.
    """
    for i in range(1, G.order() + 1):
        for S in combinations(G.nodes(), i):
            if is_k_power_dominating_set(G, S, k):
                return list(S)


def k_power_domination_number(G, k):
    """Return the k-power domination number of *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The k-power domination number of *G*.
    """
    return len(min_k_power_dominating_set(G, k))


def is_power_dominating_set(G, nodes):
    """Return whether or not the nodes in `nodes` comprise a power dominating
    set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    Returns
    -------
    boolean
        True if the nodes in `nodes` comprise a power dominating set, False
        otherwise.
    """
    return is_k_power_dominating_set(G, nodes, 1)


def min_power_dominating_set(G):
    """Return a smallest power dominating set of nodes in *G*.

    The method used to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest power dominating set in *G*.
    """
    return min_k_power_dominating_set(G, 1)


def power_domination_number(G):
    """Return the power domination number of *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The power domination number of *G*.
    """
    return k_power_domination_number(G, 1)
