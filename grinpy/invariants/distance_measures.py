# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing distance-related invariants in a graph"""

import itertools
import functools

from grinpy.functions.distance import distance


def triameter(G):
    r"""Returns the triameter of the graph G with at least 3 nodes.

    The *triameter* of a connected graph G with vertex set *V* is defined as the
    following maximum value

    .. math::
        \max\{d(v,w) + d(w,z) + d(v,z): v,w,z \in V: \}

    Parameters
    ----------
    G : NetworkX graph
        An undirected connected graph with order at least 3.

    Returns
    -------
    int
        The triameter of the graph G.

    References
    ----------
    A. Das, The triameter of graphs, ArXiv preprint arXiv:1804.01088, 2018.
    https://arxiv.org/pdf/1804.01088.pdf
    """
    _distance = functools.partial(distance, G)
    distance_sums = (
        sum((_distance(*pair) for pair in itertools.combinations(nodes, 2)))
        for nodes in itertools.combinations(G.nodes(), 3)
    )
    return max(distance_sums)
