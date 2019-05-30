# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Assorted degree related graph utilities.
"""

import collections
from grinpy import degree, nodes, number_of_nodes
from grinpy.functions.neighborhoods import closed_neighborhood, neighborhood, set_neighborhood, set_closed_neighborhood

__all__ = [
    "degree_sequence",
    "min_degree",
    "max_degree",
    "average_degree",
    "number_of_nodes_of_degree_k",
    "number_of_degree_one_nodes",
    "number_of_min_degree_nodes",
    "number_of_max_degree_nodes",
    "neighborhood_degree_list",
    "closed_neighborhood_degree_list",
    "is_regular",
    "is_k_regular",
    "is_sub_cubic",
    "is_cubic",
]


def degree_sequence(G):
    """Return the degree sequence of G.

    The degree sequence of a graph is the sequence of degrees of the nodes
    in the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        The degree sequence of the graph.

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.degree_sequence(G)
    [1, 2, 1]
    """
    return [degree(G, v) for v in nodes(G)]


def min_degree(G):
    """Return the minimum degree of G.

    The minimum degree of a graph is the smallest degree of any node in the
    graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The minimum degree of the graph.

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.min_degree(G)
    1
    """
    D = degree_sequence(G)
    D.sort()
    return D[0]


def max_degree(G):
    """Return the maximum degree of G.

    The maximum degree of a graph is the largest degree of any node in the
    graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The maximum degree of the graph.

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.min_degree(G)
    2
    """
    D = degree_sequence(G)
    D.sort(reverse=True)
    return D[0]


def average_degree(G):
    """Return the average degree of G.

    The average degree of a graph is the average of the degrees of all nodes
    in the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The average degree of the graph.

    Examples
    --------
    >>> G = nx.star_graph(3) # Star on 4 nodes
    >>> nx.average_degree(G)
    1.5
    """
    return sum(degree_sequence(G)) / number_of_nodes(G)


def number_of_nodes_of_degree_k(G, k):
    """Return the number of nodes of the graph with degree equal to k.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    int
        The number of nodes in the graph with degree equal to k.

    See Also
    --------
    number_of_leaves, number_of_min_degree_nodes, number_of_max_degree_nodes

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_nodes_of_degree_k(G, 1)
    2
    """
    return sum(1 for v in nodes(G) if degree(G, v) == k)


def number_of_degree_one_nodes(G):
    """Return the number of nodes of the graph with degree equal to 1.

    A vertex with degree equal to 1 is also called a *leaf*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The number of nodes in the graph with degree equal to 1.

    See Also
    --------
    number_of_nodes_of_degree_k, number_of_min_degree_nodes,
    number_of_max_degree_nodes

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_leaves(G)
    2
    """
    return number_of_nodes_of_degree_k(G, 1)


def number_of_min_degree_nodes(G):
    """Return the number of nodes of the graph with degree equal to the minimum
    degree of the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The number of nodes in the graph with degree equal to the minimum
        degree.

    See Also
    --------
    number_of_nodes_of_degree_k, number_of_leaves, number_of_max_degree_nodes,
    min_degree

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_min_degree_nodes(G)
    2
    """
    return number_of_nodes_of_degree_k(G, min_degree(G))


def number_of_max_degree_nodes(G):
    """Return the number of nodes of the graph with degree equal to the maximum
    degree of the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The number of nodes in the graph with degree equal to the maximum
        degree.

    See Also
    --------
    number_of_nodes_of_degree_k, number_of_leaves, number_of_min_degree_nodes,
    max_degree

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_max_degree_nodes(G)
    1
    """
    return number_of_nodes_of_degree_k(G, max_degree(G))


def neighborhood_degree_list(G, nbunch):
    """Return a list of the unique degrees of all neighbors of nodes in
    `nbunch`.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container of nodes.

    Returns
    -------
    list
        A list of the degrees of all nodes in the neighborhood of the nodes
        in `nbunch`.

    See Also
    --------
    closed_neighborhood_degree_list, neighborhood

    Examples
    --------
    >>> import grinpy as gp
    >>> G = gp.path_graph(3) # Path on 3 nodes
    >>> gp.neighborhood_degree_list(G, 1)
    [1, 2]
    """
    if isinstance(nodes, collections.abc.Iterable):
        return list(set(degree(G, u) for u in set_neighborhood(G, nbunch)))
    else:
        return list(set(degree(G, u) for u in neighborhood(G, nbunch)))


def closed_neighborhood_degree_list(G, nbunch):
    """Return a list of the unique degrees of all nodes in the closed
    neighborhood of the nodes in `nbunch`.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container of nodes.

    Returns
    -------
    list
        A list of the degrees of all nodes in the closed neighborhood of the
        nodes in `nbunch`.

    See Also
    --------
    closed_neighborhood, neighborhood_degree_list

    Examples
    --------
    >>> import grinpy as gp
    >>> G = gp.path_graph(3) # Path on 3 nodes
    >>> gp.closed_neighborhood_degree_list(G, 1)
    [1, 2, 2]
    """
    if isinstance(nodes, collections.abc.Iterable):
        return list(set(degree(G, u) for u in set_closed_neighborhood(G, nbunch)))
    else:
        return list(set(degree(G, u) for u in closed_neighborhood(G, nbunch)))


def is_regular(G):
    """ Return True if G is regular, and False otherwise.

    A graph is *regular* if each node has the same degree.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph

    Returns
    -------
    boolean
        True if regular, false otherwise.
    """
    return min_degree(G) == max_degree(G)


def is_k_regular(G, k):
    """ Return True if the graph is regular of degree k and False otherwise.

    A graph is *regular of degree k* if all nodes have degree equal to *k*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph

    k : int
        An integer

    Returns
    -------
    boolean
        True if all nodes have degree equal to *k*, False otherwise.
    """
    # check that k is an integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    for v in nodes(G):
        if not degree(G, v) == k:
            return False
    return True


def is_sub_cubic(G):
    """ Return True if *G* sub-cubic, and False otherwise.

    A graph is *sub-cubic* if its maximum degree is at most 3.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    boolean
        True if *G* is sub-cubic, False otherwise.
    """
    return max_degree(G) <= 3


def is_cubic(G):
    """ Return True if *G* is cubic, and False otherwise.

    A graph is *cubic* if it is regular of degree 3.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph

    Returns
    -------
    boolean
        True if *G* is cubic, False otherwise.
    """
    return is_k_regular(G, 3)
