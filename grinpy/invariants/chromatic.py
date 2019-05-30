# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing the chromatic number of a graph."""

import itertools

import numpy as np
from pulp import LpBinary, LpMinimize, LpProblem, LpVariable, lpSum

from grinpy import is_connected
from grinpy.functions.graph_operations import contract_nodes
from grinpy.functions.neighborhoods import are_neighbors, common_neighbors
from grinpy.functions.structural_properties import is_complete_graph
from grinpy.utils.combinations import pairs_of_nodes

__all__ = ["chromatic_number", "min_proper_coloring"]


def min_proper_coloring_ilp(G):
    """Return a smallest proper coloring the graph.

    A *k*-proper coloring is a function

    .. math::

        c : V \\to \\{1, \\dotsb, k\\} \\mthrm{ such that } c(u) \\neq c(v)
        \\mathrm{ for all } \\{u, v\\} \\in E

    where *V* and *E* are the vertex and edge set of *G*.

    A smallest proper coloring is a proper coloring with minimum *k*.

    This method using integer programming to compute a smallest proper
    coloring. It solves the following integer linear program: minimize

    .. math::

        \\sum_{1 \\leq j \\leq n} x_j


    subject to

    .. math::

        \\sum_{1 \\leq j \\leq n} c_v^j = 1 \\mathrm{ for all } v \\in V
        c_v^j + c_u^j \\leq 1 \\mathrm{ for all } j \\in \\{1, \\dotsb, n\\}, \\{u, v\\} \\in E
        c_v^j \\leq y_j \\mathrm{ for all } j \\in \\{1, \\dotsb, n\\}, v \\in V
        y_j, c_v^j \\in \\{0, 1\\} \\mathrm{ for all } j \\in \\{1, \\dotsb, n\\}, v \\in V

    Note that this method is not imported by default when importing
    GrinPy. See `min_proper_coloring`.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    dict
        A dictionary whose keys are colors and values are sets of
        nodes colored that color in a smallest proper coloring.

    See Also
    --------
    min_proper_coloring

    """
    prob = LpProblem("min_proper_coloring", LpMinimize)
    colors = {i: LpVariable("x_{}".format(i), 0, 1, LpBinary) for i in range(G.order())}
    node_colors = {
        node: [LpVariable("c_{}_{}".format(node, i), 0, 1, LpBinary) for i in range(G.order())] for node in G.nodes()
    }

    # Set the min proper coloring objective function
    prob += lpSum([colors[i] for i in colors])

    # Set constraints
    for node in G.nodes():
        prob += sum(node_colors[node]) == 1

    for edge, i in itertools.product(G.edges(), range(G.order())):
        prob += sum(node_colors[edge[0]][i] + node_colors[edge[1]][i]) <= 1

    for node, i in itertools.product(G.nodes(), range(G.order())):
        prob += node_colors[node][i] <= colors[i]

    prob.solve()
    solution_set = {color: [node for node in node_colors if node_colors[node][color].value() == 1] for color in colors}
    return solution_set


def min_proper_coloring(G):
    """Return a smallest proper coloring the graph.

    A *k*-proper coloring is a function

    .. math::

        c : V \\to \\{1, \\dotsb, k\\} \\mthrm{ such that } c(u) \\neq c(v)
        \\mathrm{ for all } \\{u, v\\} \\in E

    where *V* and *E* are the vertex and edge set of *G*.

    A smallest proper coloring is a proper coloring with minimum *k*.

    This method using integer programming to compute a smallest proper
    coloring by calling the `min_proper_coloring_ilp` method.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    dict
        A dictionary whose keys are colors and values are sets of
        nodes colored that color in a smallest proper coloring.

    See Also
    --------
    min_proper_coloring_ilp

    """
    return min_proper_coloring_ilp(G)


def chromatic_number_ilp(G):
    """
    Return the chromatic number of G.

    This method calculates the chromatic number by solving an integer
    linear program.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The chromatic number of G.

    """
    coloring = min_proper_coloring_ilp(G)
    colors = [color for color in coloring if len(coloring[color]) > 0]
    return len(colors)


def chromatic_number_ram_rama(G):
    """Return the chromatic number of G.

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
    if not is_connected(G):
        raise TypeError("Invalid graph: not connected")

    if is_complete_graph(G):
        return G.order()

    # get list of pairs of non neighbors in G
    N = [list(p) for p in pairs_of_nodes(G) if not are_neighbors(G, p[0], p[1])]

    # get a pair of non neighbors who have the most common neighbors
    num_common_neighbors = list(map(lambda p: len(common_neighbors(G, p)), N))
    P = N[np.argmax(num_common_neighbors)]

    # Collapse the nodes in P and repeat the above process
    H = G.copy()
    contract_nodes(H, P)
    return chromatic_number(H)


def chromatic_number(G, method="ilp"):
    """Return the chromatic number of G.

    The *chromatic number* of a graph G is the size of a mininum
    coloring of the nodes in G such that no two adjacent nodes have the
    same color.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    method: string
        The method to use for finding the maximum matching. Use
        'ilp' for integer linear program or 'ram-rama' for the Ram-Rama
        algorithm. Defaults to 'ilp'.

    Returns
    -------
    set
        A set of edges comprising a maximum matching in *G*.

    See Also
    --------
    max_matching

    """
    chromatic_number_func = {"ram-rama": chromatic_number_ram_rama, "ilp": chromatic_number_ilp}.get(method, None)

    if chromatic_number_func:
        return chromatic_number_func(G)

    raise ValueError('Invalid `method` argument "{}"'.format(method))
