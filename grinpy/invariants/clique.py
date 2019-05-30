# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing independence related invariants for a graph."""

from grinpy import graph_clique_number

__all__ = ["clique_number"]


def clique_number(G, cliques=None):
    """Return the clique number of the graph.

    A *clique* in a graph *G* is a complete subgraph. The *clique number* is the
    size of a largest clique.

    This function is a wrapper for the NetworkX :func:`graph_clique_number`
    method in `networkx.algorithms.clique`.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    cliques : list
        A list of cliques, each of which is itself a list of nodes. If not
        specified, the list of all cliques will be computed, as by
        :func:`networkx.algorithms.clique.find_cliques()`.

    Returns
    -------
    int
        The size of a largest clique in `G`

    Notes
    --------
    You should provide `cliques` if you have already computed the list of
    maximal cliques, in order to avoid an exponential time search for maximal
    cliques.
    """
    return graph_clique_number(G, cliques)
