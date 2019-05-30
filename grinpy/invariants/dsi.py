# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing DSI style invariants."""


from grinpy import degree_sequence, number_of_edges

__all__ = ["sub_k_domination_number", "slater", "sub_total_domination_number", "annihilation_number"]


# methods
def sub_k_domination_number(G, k):
    r"""Return the sub-k-domination number of the graph.

    The *sub-k-domination number* of a graph G with *n* nodes is defined as the
    smallest positive integer t such that the following relation holds:

    .. math::
        t + \frac{1}{k}\sum_{i=0}^t d_i \geq n

    where

    .. math::
        {d_1 \geq d_2 \geq \cdots \geq d_n}

    is the degree sequence of the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    int
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
    D. Amos, J. Asplund, B. Brimkov and R. Davila, The sub-k-domination number
    of a graph with applications to k-domination, *arXiv preprint
    arXiv:1611.02379*, (2016)
    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    if k < 1:
        raise ValueError("Expected k to be a positive integer.")
    D = degree_sequence(G)
    D.sort(reverse=True)
    n = len(D)
    for i in range(n + 1):
        if i + (sum(D[:i]) / k) >= n:
            return i
    # if above loop completes, return None
    return None


def slater(G):
    r"""Return the Slater invariant for the graph.

    The Slater invariant of a graph G is a lower bound for the domination
    number of a graph defined by:

    .. math::
        sl(G) = \min\{t : t + \sum_{i=0}^t d_i \geq n\}

    where

    .. math::
        {d_1 \geq d_2 \geq \cdots \geq d_n}

    is the degree sequence of the graph ordered in non-increasing order and *n*
    is the order of G.

    Amos et al. rediscovered this invariant and generalized it into what is
    now known as the sub-*k*-domination number.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The Slater invariant for the graph.

    See Also
    --------
    sub_k_domination_number

    References
    ----------
    D. Amos, J. Asplund, B. Brimkov and R. Davila, The sub-k-domination number
    of a graph with applications to k-domination, *arXiv preprint
    arXiv:1611.02379*, (2016)

    P.J. Slater, Locating dominating sets and locating-dominating set, *Graph
    Theory, Combinatorics and Applications: Proceedings of the 7th Quadrennial
    International Conference on the Theory and Applications of Graphs*,
    2: 2073-1079 (1995)
    """
    return sub_k_domination_number(G, 1)


def sub_total_domination_number(G):
    r"""Return the sub-total domination number of the graph.

    The sub-total domination number is defined as:

    .. math::
        sub_{t}(G) = \min\{t : \sum_{i=0}^t d_i \geq n\}

    where

    .. math::
        {d_1 \geq d_2 \geq \cdots \geq d_n}

    is the degree sequence of the graph ordered in non-increasing order and *n*
    is the order of the graph.

    This invariant was defined and investigated by Randy Davila.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The sub-total domination number of the graph.

    References
    ----------
    R. Davila, A note on sub-total domination in graphs. *arXiv preprint
    arXiv:1701.07811*, (2017)
    """
    D = degree_sequence(G)
    D.sort(reverse=True)
    n = len(D)
    for i in range(n + 1):
        if sum(D[:i]) >= n:
            return i
    # if above loop completes, return None
    return None


def annihilation_number(G):
    r"""Return the annihilation number of the graph.

    The annihilation number of a graph G is defined as:

    .. math::
        a(G) = \max\{t : \sum_{i=0}^t d_i \leq m\}

    where

    .. math::
        {d_1 \leq d_2 \leq \cdots \leq d_n}

    is the degree sequence of the graph ordered in non-decreasing order and *m*
    is the number of edges in G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The annihilation number of the graph.
    """
    D = degree_sequence(G)
    D.sort()  # sort in non-decreasing order
    n = len(D)
    m = number_of_edges(G)
    # sum over degrees in the sequence until the sum is larger than the number of edges in the graph
    for i in reversed(range(n + 1)):
        if sum(D[:i]) <= m:
            return i
