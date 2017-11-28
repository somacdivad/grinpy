# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing the residue and related invariants."""

from grinpy import havel_hakimi_process, elimination_sequence

__all__ = ['residue',
           'k_residue'
          ]

def residue(G):
    """Return the *residue* of *G*.

    The *residue* of a graph *G* is the number of zeros obtained in final
    sequence of the Havel Hakimi process.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    residue : int
        The residue of *G*.

    See Also
    --------
    k_residue, havel_hakimi_process
    """
    return havel_hakimi_process(G).residue()

def k_residue(G, k):
    """Return the *k-residue* of *G*.

    The *k-residue* of a graph *G* is defined as follows:

    .. math::
        \frac{1}{k}\sum_{i=0}^{k-1}(k - i)f(i)

    where *f(i)* is the frequency of *i* in the elmination sequence of the
    graph. The elimination sequence is the sequence of deletions made during the
    Havel Hakimi process together with the zeros obtained in the final step.

    Parameters
    ----------
    G : graph
        A Networkx graph.

    Returns
    -------
    kResidue : float
        The k-residue of *G*.

    See Also
    --------
    residue, havel_hakimi_process, elimination_sequence
    """
    E = elimination_sequence(G)
    return sum((k - i) * E.count(i) for i in range(k)) / k
