# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
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

__all__ = ['max_matching',
           'max_matching_ip',
           'matching_number',
           'min_maximal_matching',
           'min_maximal_matching_number'
           ]


def max_matching(G):
    """Return a maximum matching in G.

    A *maximum matching* is a largest set of edges such that no two edges in
    the set have a common endpoint.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of edges in a maximum matching.
    """
    if number_of_edges(G) == 0:
        return []
    for i in reversed(range(1, number_of_edges(G) + 1)):
        for S in combinations(edges(G), i):
            if is_matching(G, set(S)):
                return list(S)


def max_matching_ip(G):
    """Return a largest matching in *G*.

    This method uses integer programming to solve for a maximum matching.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of edges comprising a maximum matching in *G*.

    See Also
    --------
    max_matching
    """
    prob = LpProblem('min_total_dominating_set', LpMaximize)
    variables = {
        edge: LpVariable('x{}'.format(i+1), 0, 1, LpBinary)
        for i, edge in enumerate(G.edges())
    }
    # Set the domination number objective function
    prob += lpSum(variables)
    # Set constraints for independence
    for node in G.nodes():
        incident_edges = [
            variables[edge]
            for edge in variables if node in edge
        ]
        prob += sum(incident_edges) <= 1
    prob.solve()
    solution_set = [edge for edge in variables if variables[edge].value() == 1]
    return solution_set


def matching_number(G):
    """Return the matching number of G.

    The *matching number* of a graph G is the cardinality of a maximum matching
    in G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The matching number of G.
    """
    return len(max_matching_ip(G))


def min_maximal_matching(G):
    """Return a smallest maximal matching in G.

    A *maximal matching* is a maximal set of edges such that no two edges in
    the set have a common endpoint.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of edges in a smalles maximal matching.
    """
    # return empty list if graph has no edges
    if number_of_edges(G) == 0:
        return []
    # loop through subsets of edges of G in decreasing order of size until a matching is found
    for i in range(1, number_of_edges(G) + 1):
        for S in combinations(edges(G), i):
            if is_maximal_matching(G, set(S)):
                return list(S)


def min_maximal_matching_number(G):
    """Return the minimum maximal matching number of G.

    The *minimum maximal matching number* of a graph G is the cardinality of a
    smallest maximal matching in G.

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
