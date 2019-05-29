# -*- coding: utf-8 -*-

#    Copyright (C) 2017---2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing the topological indicies of a graph.

Many of these indicies were developed in relation to chemical graph theory, and
some have been related to quantum theory.
"""

import functools
import math

import networkx as nx

__all__ = [
    "randic_index",
    "augmented_randic_index",
    # "harmonic_index",
    # "atom_bond_connectivity_index",
    # "sum_connectivity_index",
]


def randic_index(G):
    r"""Returns the Randic Index of the graph G.

    The *Randic index* of a graph *G* with edge set *E* is defined as the
    following sum:

    .. math::
        \sum_{vw \in E} \frac{1}{\sqrt(d_G(v)*d_G(w))}

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The Randic Index of a graph.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return math.fsum(((_degree(e[0]) * _degree(e[1])) ** -0.5 for e in G.edges()))


def augmented_randic_index(G):
    r"""Returns the augmented Randic Index of the graph G.

    The *augmented-Randic index* of a graph G with edge set *E* is defined as the
    following sum

    .. math::
        \sum_{vw \in E} \frac{1}{\max(d_G(v), d_G(w))}

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The augmented Randic index of a graph.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return math.fsum((max(_degree(x), _degree(y)) ** -1 for x, y in G.edges()))
