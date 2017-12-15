# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing neighborhoods of vertices and sets of vertices."""

from grinpy import neighbors

def neighborhood(G, nbunch):
    """Return a list of all neighbors of the nodes in nbunch.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch : a single node or iterable container

    Returns
    -------
    list
        A list containing all nodes that are a neighbor of some node in nbunch.

    See Also
    --------
    closed_neighborhood

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.neighborhood(G, 1)
    [0, 2]
    """
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    # loop through all nodes in nbunch and add their neighbors to the set of neighbors
    N = set()
    for v in nbunch:
        N |= set(neighbors(G, v))
    return list(N)

def closed_neighborhood(G, nbunch):
    """Return a list of all neighbors of the nodes in nbunch, including the
    nodes in nbunch.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nbunch : a single node or iterable container

    Returns
    -------
    list
        A list containing all nodes that are a neighbor of some node in nbunch
        together with all nodes in nbunch.

    See Also
    --------
    neighborhood

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.closed_neighborhood(G, 1)
    [0, 1, 2]
    """
    # check if nbunch is an iterable; if not, convert to a list
    try:
        _ = (v for v in nbunch)
    except:
        nbunch = [nbunch]
    N = set(neighborhood(G, nbunch)).union(nbunch)
    return list(N)

def are_neighbors(G, v, nbunch):
    """Returns true if v is adjacent to any of the nodes in nbunch. Otherwise,
    returns false.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    v : node
        A node in the graph.

    nbunch : a single node or iterable container

    Returns
    -------
    bool
        If nbunch in a single node, True if v in a neighbor that node and False
        otherwise.

        If nbunch is an interable, True if v is a neighbor of some node in
        nbunch and False otherwise.


    Examples
    --------
    >>> G = nx.star_graph(3) # Star on 4 nodes
    >>> nx.are_neighbors(G, 0, 1)
    True
    >>> nx.are_neighbors(G, 1, 2)
    False
    >>> nx.are_neighbors(G, 1, [0, 2])
    True
    """
    return v in neighborhood(G, nbunch)
