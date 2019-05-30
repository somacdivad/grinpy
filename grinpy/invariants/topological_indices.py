# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
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
    "generalized_randic_index",
    "augmented_randic_index",
    "harmonic_index",
    "atom_bond_connectivity_index",
    "sum_connectivity_index",
    "first_zagreb_index",
    "second_zagreb_index",
]


def _topological_index(G, func):
    """Return the topological index of ``G`` determined by ``func``"""

    return math.fsum(func(*edge) for edge in G.edges())


def randic_index(G):
    r"""Returns the Randić Index of the graph ``G``.

    The *Randić index* of a graph *G* with edge set *E* is defined as the
    following sum:

    .. math::
        \sum_{vw \in E} \frac{1}{\sqrt{d_G(v) \times d_G(w)}}

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The Randić Index of a ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(G, func=lambda x, y: 1 / math.sqrt(_degree(x) * _degree(y)))


def generalized_randic_index(G, k):
    r"""Returns the generalized Randić Index of the graph ``G``.

    The *generalized Randić index* of a graph *G* with edge set *E* is defined as the
    following sum:

    .. math::
        \sum_{vw \in E} \big(d_G(v) \times d_G(w)\big)^{k}

    where `k` is some real number.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : float
        Exponent parameter for generalized Randić index.

    Returns
    -------
    float
        The generalized Randić Index of a ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(G, func=lambda x, y: pow(_degree(x) * _degree(y), k))


def augmented_randic_index(G):
    r"""Returns the augmented Randić Index of the graph ``G``.

    The *augmented Randić index* of a graph G with edge set *E* is defined as the
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
        The augmented Randic index of ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294

    *Note*: The above reference appears to be wrong. Help with the correct reference is greatly appreciated.
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(G, func=lambda x, y: 1 / max(_degree(x), _degree(y)))


def harmonic_index(G):
    r"""Returns the Harmonic Index of the graph ``G``.

    The *harmonic index* of a graph *G* with edge set *E* is defined as the
    following sum:

    .. math::
        \sum_{vw \in E} \frac{2}{d_G(v) + d_G(w)}

    This invariant was originally introduced by Siemion Fajtlowicz.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The harmonic index of ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(G, func=lambda x, y: 2 / (_degree(x) + _degree(y)))


def atom_bond_connectivity_index(G):
    r"""Returns the atom bond connectivity Index of the graph ``G``.

    The *atom bond connectivity index* of a graph *G* with edge set *E* is defined as the
    following sum:

    .. math::
        \sum_{vw \in E} \sqrt{\frac{d_G(v) + d_G(w) - 2)}{d_G(v) \times d_G(w)}}

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The atom bond connectivity index of ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(
        G, func=lambda x, y: math.sqrt((_degree(x) + _degree(y) - 2) / (_degree(x) * _degree(y)))
    )


def sum_connectivity_index(G):
    r"""Returns the sum connectivity index of the graph ``G``.

    The *sum connectivity index* of a graph *G* with edge set *E* is defined as the
    following sum:

    .. math::
        \sum_{vw \in E} \frac{1}{\sqrt{d_G(v) + d_G(w)}}

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The sum connectivity index of ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(G, func=lambda x, y: 1 / math.sqrt(_degree(x) + _degree(y)))


def first_zagreb_index(G):
    r"""Returns the first Zagreb index of the graph ``G``.

    The *first Zagreb index* of a graph *G* with vertex set *V* is defined as the
    following sum:

    .. math::
        \sum_{v \in E} d_G(v)^{2}

    Remarkably, this sum is equiavlent to the following:

    .. math::
        \sum_{vw \in E} d_G(v) + d_G(w)

    where *E* is the edge set of *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The first Zagreb index of ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(G, func=lambda x, y: _degree(x) + _degree(y))


def second_zagreb_index(G):
    r"""Returns the second Zagreb index of the graph ``G``.

    The *second Zagreb index* of a graph *G* with edge set *E* is defined as the
    following sum:

    .. math::
        \sum_{vw \in E} d_G(v) \times d_G(w)

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The second Zagreb index of ``G``.

    References
    ----------

    Ivan Gutman, Degree-Based Topological Indices, Croat. Chem. Acta 86 (4)
    (2013) 351–361. http://dx.doi.org/10.5562/cca2294
    """
    _degree = functools.partial(nx.degree, G)
    return _topological_index(G, func=lambda x, y: _degree(x) * _degree(y))
