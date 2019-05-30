# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing the residue and related invariants."""

from grinpy import havel_hakimi_process, elimination_sequence
from grinpy.invariants.independence import independence_number

__all__ = ["residue", "k_residue", "k_residual_index"]


def residue(G):
    """Return the *residue* of *G*.

    The *residue* of a graph *G* is the number of zeros obtained in final
    sequence of the Havel Hakimi process.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The residue of *G*.

    See Also
    --------
    k_residue, havel_hakimi_process
    """
    return havel_hakimi_process(G).residue()


def k_residue(G, k):
    r"""Return the *k-residue* of *G*.

    The *k-residue* of a graph *G* is defined as follows:

    .. math::
        \frac{1}{k}\sum_{i=0}^{k-1}(k - i)f(i)

    where *f(i)* is the frequency of *i* in the elmination sequence of the
    graph. The elimination sequence is the sequence of deletions made during the
    Havel Hakimi process together with the zeros obtained in the final step.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    float
        The k-residue of *G*.

    See Also
    --------
    residue, havel_hakimi_process, elimination_sequence
    """
    E = elimination_sequence(G)
    return sum((k - i) * E.count(i) for i in range(k)) / k


def k_residual_index(G):
    """Return the k-residual_index of G.

    The *k-residual index* of a graph *G* is the smallest integer k such that
    the k-residue of *G* is greathe than or equal to the independence number of
    *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The smallest integer k such that k_residue(G,k) >= independence_number(G).

    See Also
    --------
    k_independence_number, k_residue

    Notes
    -----
    It should be noted that the k-residual index was originally conjectured to
    be an upper bound on the independence number by Siemion Faijtlowizc and
    his original conjecturing program Graffiti. This was told to Davila by
    personal communication with Ryan Pepper, a former PhD student of
    Faijtlowicz.
    """
    k = 1
    while k_residue(G, k) < independence_number(G):
        k += 1
    return k
