# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing disparity related invariants.
"""

from grinpy.functions.degree import closed_neighborhood_degree_list, neighborhood_degree_list

__all__ = ['vertex_disparity',
           'closed_vertex_disparity',
           'disparity_sequence',
           'closed_disparity_sequence',
           'disparity',
           'closed_disparity',
           'CW_disparity',
           'closed_CW_disparity',
           'inverse_disparity',
           'closed_inverse_disparity',
           'disparity_average',
           'closed_disparity_average',
           'k_disparity',
           'closed_k_disparity'
          ]

def vertex_disparity(G, v):
    # TODO: Add documentation
    return len(neighborhood_degree_list(G, v))

def closed_vertex_disparity(G, v):
    # TODO: Add documentation
    return len(closed_neighborhood_degree_list(G, v))

def disparity_sequence(G):
    # TODO: Add documentation
    return [vertex_disparity(G, v) for v in vertices(G)]

def closed_disparity_sequence(G):
    # TODO: Add documentation
    return [closed_vertex_disparity(G, v) for v in vertices(G)]

def disparity(G):
    # TODO: Add documentation
    return sum(disparity_sequence(G))

def closed_disparity(G):
    # TODO: Add documentation
    return sum(closed_disparity_sequence(G))

def CW_disparity(G):
    # TODO: Add documentation
    D = list(map(lambda x: 1 / (1 + x), disparity_sequence(G)))
    return sum(D)

def closed_CW_disparity(G):
    # TODO: Add documentation
    D = list(map(lambda x: 1 / (1 + x), closed_disparity_sequence(G)))
    return sum(D)

def inverse_disparity(G):
    # TODO: Add documentation
    D = list(map(lambda x: 1 / x, disparity_sequence(G)))
    return sum(D)

def closed_inverse_disparity(G):
    # TODO: Add documentation
    D = list(map(lambda x: 1 / x, closed_disparity_sequence(G)))
    return sum(D)

def disparity_average(G):
    # TODO: Add documentation
    D = disparity_sequence(G)
    return sum(D) / len(D)

def closed_disparity_average(G):
    # TODO: Add documentation
    D = closed_disparity_sequence(G)
    return sum(D) / len(D)

def k_disparity(G, k):
    # TODO: Add documentation
    D = disparity_sequence(G)
    s = 0
    for i in range(k):
        s += (k - i) * D.count(i)
    return (2 * s) / (k * (k+1))

def closed_k_disparity(G, k):
    # TODO: Add documentation
    D = closed_disparity_sequence(G)
    s = 0
    for i in range(k):
        s += (k - i) * D.count(i)
    return (2 * s) / (k * (k+1))
