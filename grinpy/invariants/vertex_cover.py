# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing vertex covers and related invariants in a graph."""


from pulp import LpBinary, LpMinimize, LpProblem, LpVariable, lpSum


def min_vertex_cover_ilp(G):
    """Return a smallest vertex cover in the graph G.

    This method uses an ILP to solve for a smallest vertex cover.
    Specifically, the ILP minimizes

    .. math::

        \\sum_{v \\in V} x_v

    subject to

    .. math::

        x_v + x_u \\geq 1 \\mathrm{for all } \\{u, v\\} \\in E
        x_v \\in \\{0, 1\\} \\mathrm{for all } v \\in V

    where *V* and *E* are the vertex and edge sets of *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    set
        A set of nodes in a smallest vertex cover.

    """
    prob = LpProblem("min_vertex_cover", LpMinimize)
    variables = {node: LpVariable("x{}".format(i + 1), 0, 1, LpBinary) for i, node in enumerate(G.nodes())}

    # Set the total domination number objective function
    prob += lpSum([variables[n] for n in variables])

    # Set constraints
    for edge in G.edges():
        prob += variables[edge[0]] + variables[edge[1]] >= 1

    prob.solve()
    solution_set = {node for node in variables if variables[node].value() == 1}
    return solution_set


def min_vertex_cover(G, method="ilp"):
    """Return a smallest vertex cover of G.

    A *vertex cover* of a graph *G* is a set of vertices with the
    property that every edge in the graph is incident to at least one
    vertex in the set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    method: string
        The method to use for finding a smallest vertex cover.
        Currently, the only option is 'ilp'. Defaults to 'ilp'.

    Returns
    -------
    set
        A set of nodes in a smallest vertex cover.

    """
    vertex_cover_func = {"ilp": min_vertex_cover_ilp}.get(method, None)

    if vertex_cover_func:
        return vertex_cover_func(G)

    raise ValueError('Invalid `method` argument "{}"'.format(method))


def vertex_cover_number(G):
    """Return a the size of smallest vertex cover in the graph G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    number
        The size of a smallest vertex cover of G.

    """
    return len(min_vertex_cover_ilp(G))
