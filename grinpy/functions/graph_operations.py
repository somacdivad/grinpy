# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for performing operations on graphs"""

from collections.abc import Iterable

from grinpy.functions.neighborhoods import neighborhood


def contract_nodes(G, nbunch, new_node=None):
    """ Contract the nodes in nbunch.

    Contracting a set S of nodes in a graph G first removes the nodes in S from
    G then creates a new node *v* with new edges *(v, u)* for all nodes *u* that
    are neighbors of a nodes in S.

    Parameters
    ----------

    G : NetworkX graph
        An undirected graph.

    nbunch :
        A single node or iterable container of nodes in G.

    new_node :
        The node to be added. If no node is given, it defaults to the minimum
        node in nbunch according to the natural ordering of nodes.

    Notes
    -----
    This method does not return a value. It alters the graph in place.
    """
    # check if nbunch is an iterable; if not, convert to a list
    if not isinstance(nbunch, Iterable):
        nbunch = [nbunch]

    nbunch = [n for n in nbunch if n in G]
    # get all neighbors of nodes in nbunch that are not also in nbunch
    N = set().union(*[neighborhood(G, n) for n in nbunch]).difference(nbunch)
    # remove the nodes in nbunch from G, then add a new node with approriate edges
    G.remove_nodes_from(nbunch)
    new_node = new_node or min(nbunch)
    G.add_node(new_node)
    G.add_edges_from(map(lambda n: (new_node, n), N))
