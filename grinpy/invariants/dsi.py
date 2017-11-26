# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing DSI style invariants."""


from grinpy import degree_sequence, number_of_edges

__all__ = ['sub_k_domination_number',
           'slater',
           'sub_total_domination_number',
           'annihilation_number',
           ]

# methods
def sub_k_domination_number(G, k):
    """Return the sub-k-domination number of the graph.

    The *sub-k-domination number* of a graph G with *n* nodes is defined as the
    smallest positive integer t such that the following relation holds:

    .. math::
        t + \frac{1}{k}\sum_{i=0}^t d_i \geq n

    where

    .. math::
        {d_1 \geq d_2 \geq \cdots \geq \d_n}

    is the degree sequence of the graph.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    k : int
        A positive integer.

    Returns
    -------
    sub : int
        The sub-k-domination number of a graph.

    See Also
    --------
    slater

    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> nx.sub_k_domination_number(G, 1)
    True

    References
    ----------
    D. Amos, J. Asplund, and R. Davila, The sub-k-domination number of a graph
    with applications to k-domination, *arXiv preprint arXiv:1611.02379*, (2016)
    """
    # TODO: add check that k >= 1 and throw error if not
    D = degree_sequence(G)
    D.sort(reverse = True)
    n = len(D)
    for i in range(n + 1):
        if i + (sum(D[:i]) / k) >= n:
            return i
    # if above loop completes, return None (should not occur)
    return None

def slater(G):
    # TODO: Add documentation
    return sub_k_domination_number(G, 1)

def sub_total_domination_number(G):
    # TODO: Add documentation
    D = degree_sequence(G)
    D.sort(reverse = True)
    n = len(D)
    for i in range(n + 1):
        if sum(D[:i]) >= n:
            return i
    # if above loop completes, return None (should not occur)
    return None

def annihilation_number(G):
    # TODO: Add documentation
    D = degree_sequence(G)
    D.sort() # sort in non-decreasing order
    m = number_of_edges(G)
    # sum over degrees in the sequence until the sum is larger than the number of edges in the graph
    S = [D[0]]
    while(sum(S) <= m):
        S.append(D[len(S)])
    return len(S) - 1

# TODO: add more DSI invariants (such as upper and lower annihilation numbers)
