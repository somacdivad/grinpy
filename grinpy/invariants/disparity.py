# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing disparity related invariants.
"""

from grinpy import nodes, number_of_nodes
from grinpy.functions.degree import closed_neighborhood_degree_list, neighborhood_degree_list

__all__ = ['vertex_disparity',
           'closed_vertex_disparity',
           'disparity_sequence',
           'closed_disparity_sequence',
           'CW_disparity',
           'closed_CW_disparity',
           'inverse_disparity',
           'closed_inverse_disparity',
           'average_vertex_disparity',
           'average_closed_vertex_disparity',
           'k_disparity',
           'closed_k_disparity',
           'irregularity'
          ]

def vertex_disparity(G, v):
    """Return number of distinct degrees of neighbors of v.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    v : a node in G

    Returns
    -------
    disparity : int
        The number of distinct degrees of neighbors of v.

    See Also
    --------
    closed_vertex_disparity
    """
    return len(neighborhood_degree_list(G, v))

def closed_vertex_disparity(G, v):
    """Return number of distinct degrees of nodes in the closed neighborhood
    of v.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    v : a node in G

    Returns
    -------
    closedDisparity : int
        The number of distinct degrees of nodes in the closed neighborhood
        of v.

    See Also
    --------
    vertex_disparity
    """
    return len(closed_neighborhood_degree_list(G, v))

def disparity_sequence(G):
    """Return the sequence of disparities of each node in the graph.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    disparitySequence : list
        The sequence of disparities of each node in the graph.

    See Also
    --------
    closed_disparity_sequence, vertex_disparity
    """
    return [vertex_disparity(G, v) for v in nodes(G)]

def closed_disparity_sequence(G):
    """Return the sequence of closed disparities of each node in the graph.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    disparitySequence : list
        The sequence of closed disparities of each node in the graph.

    See Also
    --------
    closed_vertex_disparity, disparity_sequence
    """
    return [closed_vertex_disparity(G, v) for v in nodes(G)]

def CW_disparity(G):
    """Return the Caro-Wei disparity of the graph.

    The *Caro-Wei disparity* of a graph is defined as:

    .. math::
        \sum_{v \in V(G)}\frac{1}{1 + disp(v)}

    where *V(G)* is the set of nodes of *G* and *disp(v)* is the disparity of
    the vertex v.

    This invariant is inspired by the Caro-Wei bound for the independence number
    of a graph, hence the name.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    cwDisparity : float
        The Caro-Wei disparity of the graph.

    See Also
    --------
    closed_CW_disparity, closed_inverse_disparity, inverse_disparity
    """
    return sum(1 / (1 + x) for x in disparity_sequence(G))

def closed_CW_disparity(G):
    """Return the closed Caro-Wei disparity of the graph.

    The *closed Caro-Wei disparity* of a graph is defined as:

    .. math::
        \sum_{v \in V(G)}\frac{1}{1 + cdisp(v)}

    where *V(G)* is the set of nodes of *G* and *cdisp(v)* is the closed
    disparity of the vertex v.

    This invariant is inspired by the Caro-Wei bound for the independence number
    of a graph, hence the name.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    closedCWDisparity : float
        The closed Caro-Wei disparity of the graph.

    See Also
    --------
    CW_disparity, closed_inverse_disparity, inverse_disparity
    """
    return sum(1 / (1 + x) for x in closed_disparity_sequence(G))

def inverse_disparity(G):
    """Return the inverse disparity of the graph.

    The *inverse disparity* of a graph is defined as:

    .. math::
        \sum_{v \in V(G)}\frac{1}{disp(v)}

    where *V(G)* is the set of nodes of *G* and *disp(v)* is the disparity
    of the vertex v.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    inverseDisparity : float
        The inverse disparity of the graph.

    See Also
    --------
    CW_disparity, closed_CW_disparity, closed_inverse_disparity
    """
    return sum(1 / x for x in disparity_sequence(G))

def closed_inverse_disparity(G):
    """Return the closed inverse disparity of the graph.

    The *closed inverse disparity* of a graph is defined as:

    .. math::
        \sum_{v \in V(G)}\frac{1}{cdisp(v)}

    where *V(G)* is the set of nodes of *G* and *cdisp(v)* is the closed
    disparity of the vertex v.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    closedInverseDisparity : float
        The closed inverse disparity of the graph.

    See Also
    --------
    CW_disparity, closed_CW_disparity, inverse_disparity
    """
    return sum(1 / x for x in closed_disparity_sequence(G))

def average_vertex_disparity(G):
    """Return the average vertex disparity of the graph.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    avgDisparity : int
        The average vertex disparity of the graph.

    See Also
    --------
    average_closed_vertex_disparity, vertex_disparity
    """
    D = disparity_sequence(G)
    return sum(D) / len(D)

def average_closed_vertex_disparity(G):
    """Return the average closed vertex disparity of the graph.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    avgClosedDisparity : int
        The average closed vertex disparity of the graph.

    See Also
    --------
    average_vertex_disparity, closed_vertex_disparity
    """
    D = closed_disparity_sequence(G)
    return sum(D) / len(D)

def k_disparity(G, k):
    """Return the k-disparity of the graph.

    The *k-disparity* of a graph is defined as:

    .. math::
        \frac{2}{k(k+1)}\sum_{i=0}^{k-i}(k-i)f(i)

    where *k* is a positive integer and *f(i)* is the frequency of i in the
    disparity sequence.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    kDisparity : float
        The k-disparity of the graph.

    See Also
    --------
    closed_k_disparity
    """
    D = disparity_sequence(G)
    D.sort(reverse = True)
    s = sum((k - i) * D[i] for i in range(k))
    return (2 * s) / (k * (k+1))

def closed_k_disparity(G, k):
    """Return the closed k-disparity of the graph.

    The *closed k-disparity* of a graph is defined as:

    .. math::
        \frac{2}{k(k+1)}\sum_{i=0}^{k-1}(k-i)d_i

    where *k* is a positive integer and *d_i* is the frequency of i in the
    closed disparity sequence.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    closedKDisparity : float
        The closed k-disparity of the graph.

    See Also
    --------
    k_disparity
    """
    D = closed_disparity_sequence(G)
    D.sort(reverse = True)
    s = sum((k - i) * D[i] for i in range(k))
    return (2 * s) / (k * (k + 1))

def irregularity(G):
    """Return the irregularity measure of the graph.

    The *irregularity* of an *n*-vertex graph is defined as:

    .. math::
        \frac{2}{n(n+1)}\sum_{i=0}^{n-i}(n-i)f(i)

    where *f(i)* is the frequency of i in the
    closed disparity sequence.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    irregularity : float
        The irregularity of the graph.

    See Also
    --------
    k_disparity
    """
    return closed_k_disparity(G, number_of_nodes(G))
