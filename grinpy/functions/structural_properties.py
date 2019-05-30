# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing various structural properites."""

import grinpy as gp
from grinpy import nodes
from grinpy.functions.neighborhoods import neighborhood
import itertools

__all__ = ["is_triangle_free", "is_bull_free", "is_claw_free", "is_complete_graph"]


def is_complete_graph(G):
    """Returns True if *G* is a complete graph, and False otherwise.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    boolean
        True if G is a complete graph, False otherwise.
    """
    V = set(nodes(G))
    for v in V:
        if not set(neighborhood(G, v)) == V.difference({v}):
            return False
    return True


def is_triangle_free(G):
    """Returns True if *G* is triangle-free, and False otherwise.

    A graph is *triangle-free* if it contains no induced subgraph isomorphic to
    the complete graph on 3 vertices.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    boolean
        True if G is triangle-free, False otherwise.

    Examples
    --------
    >>> G = gp.complete_graph(4)
    >>> gp.is_triangle_free(G)
    False
    >>> G = gp.cycle_graph(5)
    >> gp.is_triangle_free(G)
    True
    """
    # define a triangle graph, also known as the complete graph K_3
    triangle = gp.complete_graph(3)

    # enumerate over all possible combinations of 3 vertices contained in G
    for S in set(itertools.combinations(G.nodes(), 3)):
        H = G.subgraph(list(S))
        if gp.is_isomorphic(H, triangle):
            return False
    # if the above loop completes, the graph is triangle free
    return True


def is_bull_free(G):
    """Returns True if *G* is bull-free, and False otherwise.

    A graph is *bull-free* if it contains no induced subgraph isomorphic to the
    bull graph, where the bull graph is the complete graph on 3 vertices with
    two pendants added to two of its vertices.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    boolean
        True if *G* is bull-free, false otherwise.

    Examples
    --------
    >>> G = gp.complete_graph(4)
    >>> gp.is_bull_free(G)
    True
    """
    # define a bull graph, also known as the graph obtained from the complete graph K_3 by addiing two pendants
    bull = gp.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (2, 4)])

    # enumerate over all possible combinations of 5 vertices contained in G
    for S in set(itertools.combinations(G.nodes(), 5)):
        H = G.subgraph(list(S))
        if gp.is_isomorphic(H, bull):
            return False
    # if the above loop completes, the graph is bull-free
    return True


def is_claw_free(G):
    """Returns True if *G* is claw-free, and False otherwise.

    A graph is *claw-free* if it contains no induce subgraph isomorphic to the
    star on four vertices.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    boolean
        True if *G* is claw-free, and False otherwise.

    Examples
    --------
    >>> G = gp.complete_graph(4)
    >>> gp.is_claw_free(G)
    True
    >>> G = gp.star_graph(4)
    >> gp.is_claw_free(G)
    False
    """
    # define a claw graph, also known as the complete bipartite graph K_1,3
    claw = gp.star_graph(3)

    # enumerate over all possible combinations of 4 vertices contained in G
    for S in set(itertools.combinations(G.nodes(), 4)):
        H = G.subgraph(list(S))
        if gp.is_isomorphic(H, claw):
            return False
    # if the above loop completes, the graph is claw-free
    return True
