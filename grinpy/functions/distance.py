# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing distances in graphs"""

import networkx as nx


def distance(G, source, target):
    r"""Return the distance in ``G`` between the ``source`` and ``target`` nodes.

    The *distance* between two nodes in a graph is the length of a
    shortest path between the nodes.

    Parameters
    ----------
    G : NetworkX graph
        An undirected connected graph with order at least 3.

    source : node in G

    target : node in G

    Returns
    -------
    int
        The distance between ``source`` and ``target`` in ``G``
    """
    return nx.shortest_path_length(G, source=source, target=target)
