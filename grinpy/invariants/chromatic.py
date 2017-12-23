# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing the chromatic number of a graph."""

from grinpy import nodes, is_connected
from grinpy.functions.graph_operations import contract_nodes
from grinpy.functions.neighborhoods import are_neighbors, common_neighbors
from grinpy.functions.structural_properties import is_complete_graph
from grinpy.utils.combinations import pairs_of_nodes
import numpy as np

__all__ = ['chromatic_number']

def chromatic_number(G):
    """ Returns the chromatic number of G.

    The *chromatic number* of a graph G is the size of a mininum coloring of
    the nodes in G such that no two adjacent nodes have the same color.

    The method for computing the chromatic number is an implementation of the
    algorithm discovered by Ram and Rama.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The chromatic number of G.

    References
    ----------
    A.M. Ram, R. Rama, An alternate method to find the chromatic number of a
    finite, connected graph, *arXiv preprint
    arXiv:1309.3642*, (2013)
    """
    if not is_connected(G): raise TypeError('Invalid graph: not connected')
    if is_complete_graph(G): return G.order()
    # get list of pairs of non neighbors in G
    N = [list(p) for p in pairs_of_nodes(G) if not are_neighbors(G, p[0], p[1])]
    # get a pair of non neighbors who have the most common neighbors
    num_common_neighbors = list(map(lambda p: len(common_neighbors(G, p)), N))
    P = N[np.argmax(num_common_neighbors)]
    # Collapse the nodes in P and repeat the above process
    H = G.copy()
    contract_nodes(H, P)
    return chromatic_number(H)
