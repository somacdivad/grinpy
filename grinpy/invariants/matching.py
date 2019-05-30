# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing matching related invariants for a graph."""

from itertools import combinations

from pulp import LpBinary, LpMaximize, LpProblem, lpSum, LpVariable

from grinpy import edges, is_matching, is_maximal_matching, number_of_edges

__all__ = ["matching_number", "min_maximal_matching", "min_maximal_matching_number"]


def max_matching_bf(G):
    """Return a maximum matching in G.

    A *maximum matching* is a largest set of edges such that no two
    edges in the set have a common endpoint.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    set
        A set of edges in a maximum matching.

    """
    if number_of_edges(G) == 0:
        return set()

    for i in reversed(range(1, number_of_edges(G) + 1)):
        for S in combinations(edges(G), i):
            if is_matching(G, set(S)):
                return set(S)


def max_matching_ilp(G):
    """Return a largest matching in *G*.

    This method uses integer programming to solve for a maximum
    matching. It solves the following integer program: maximize

    .. math::

        \\sum_{e \\in E} x_e

    subject to

    ... math::

        \\sum_{e \\sim u} x_e \\leq 1 \\mathrm{ for all } u \\in V

    where *E* and *V* are the set of edges and nodes of G, and *e* ~ *u*
    denotes "*e* is incident to *u*."

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    set
        A set of edges comprising a maximum matching in *G*.

    See Also
    --------
    max_matching

    """
    prob = LpProblem("min_total_dominating_set", LpMaximize)
    variables = {edge: LpVariable("x{}".format(i + 1), 0, 1, LpBinary) for i, edge in enumerate(G.edges())}

    # Set the maximum matching objective function
    prob += lpSum(variables)

    # Set constraints
    for node in G.nodes():
        incident_edges = [variables[edge] for edge in variables if node in edge]
        prob += sum(incident_edges) <= 1

    prob.solve()
    solution_set = {edge for edge in variables if variables[edge].value() == 1}
    return solution_set


def max_matching(G, method="ilp"):
    """Return a largest matching in *G*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    method: string
        The method to use for finding the maximum matching. Use
        'ilp' for integer linear program or 'bf' for brute force.
        Defaults to 'ilp'.

    Returns
    -------
    set
        A set of edges comprising a maximum matching in *G*.

    See Also
    --------
    max_matching

    """
    max_matching_func = {"bf": max_matching_bf, "ilp": max_matching_ilp}.get(method, None)

    if max_matching_func:
        return max_matching_func(G)

    raise ValueError('Invalid `method` argument "{}"'.format(method))


def matching_number(G, method="ilp"):
    """Return the matching number of G.

    The *matching number* of a graph G is the cardinality of a maximum
    matching in G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The matching number of G.

    """
    try:
        return len(max_matching(G, method))
    except ValueError:
        raise


def min_maximal_matching(G):
    """Return a smallest maximal matching in G.

    A *maximal matching* is a maximal set of edges such that no two
    edges in the set have a common endpoint.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    set
        A set of edges in a smallest maximal matching.

    """
    if number_of_edges(G) == 0:
        return set()

    for i in range(1, number_of_edges(G) + 1):
        for S in combinations(edges(G), i):
            if is_maximal_matching(G, set(S)):
                return set(S)


def min_maximal_matching_number(G):
    """Return the minimum maximal matching number of G.

    The *minimum maximal matching number* of a graph G is the
    cardinality of a smallest maximal matching in G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The minimum maximal matching number of G.

    """
    return len(min_maximal_matching(G))
