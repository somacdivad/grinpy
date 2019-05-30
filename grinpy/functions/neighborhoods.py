# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing neighborhoods of vertices and sets of vertices."""

from grinpy import neighbors

__all__ = [
    "neighborhood",
    "closed_neighborhood",
    "are_neighbors",
    "common_neighbors",
    "set_neighborhood",
    "set_closed_neighborhood",
]


def neighborhood(G, v):
    """Return a list of all neighbors of v.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    v :
        A node in G.

    Returns
    -------
    list
        A list containing all nodes that are a neighbor of v.

    See Also
    --------
    closed_neighborhood

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.neighborhood(G, 1)
    [0, 2]
    """
    return list(neighbors(G, v))


def set_neighborhood(G, nodes):
    """Return a list of all neighbors of every node in nodes.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes :
        An interable container of nodes in G.

    Returns
    -------
    list
        A list containing all nodes that are a neighbor of some node in nodes.

    See Also
    --------
    set_closed_neighborhood
    """
    # TODO: write unit test
    N = set()
    for n in nodes:
        N |= set(neighborhood(G, n))
    return list(N)


def closed_neighborhood(G, v):
    """Return a list with v and of all neighbors of v.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    v :
        A node in G.

    Returns
    -------
    list
        A list containing v and all nodes that are a neighbor of v.

    See Also
    --------
    neighborhood

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.closed_neighborhood(G, 1)
    [0, 1, 2]
    """
    return list(set(neighborhood(G, v)).union([v]))


def set_closed_neighborhood(G, nodes):
    """Return a list containing every node in nodes all neighbors their neighbors.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes :
        An interable container of nodes in G.

    Returns
    -------
    list
        A list containing every node in nodes and all nodes of their neighbors.

    See Also
    --------
    set_neighborhood
    """
    # TODO: write unit test
    N = set(set_neighborhood(G, nodes)).union(nodes)
    return list(N)


def are_neighbors(G, u, v):
    """Returns true if u is adjacent to v. Otherwise,
    returns false.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    u : node
        A node in the graph.

    v : node
        A node in the graph.


    Returns
    -------
    bool
        True if u is a neighbor of v in G, False otherwise.


    Examples
    --------
    >>> G = nx.star_graph(3) # Star on 4 nodes
    >>> nx.are_neighbors(G, 0, 1)
    True
    >>> nx.are_neighbors(G, 1, 2)
    False
    """
    return u in neighborhood(G, v)


def common_neighbors(G, nodes):
    """Returns a list of all nodes in G that are adjacent to every node in `nodes`.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container

    Returns
    -------
    list
        All nodes adjacent to every node in nbunch. If nbunch contains only a
        single node, that nodes neighborhood is returned.
    """
    S = set(neighborhood(G, nodes[0]))
    for n in nodes:
        S = S.intersection(set(neighborhood(G, n)))
    return list(S)
