# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing dominating sets in a graph."""
from itertools import combinations

from pulp import LpBinary, LpMinimize, LpProblem, LpVariable, lpSum

from grinpy import (
    closed_neighborhood,
    is_connected,
    is_dominating_set,
    neighborhood,
    nodes,
    number_of_nodes,
    number_of_nodes_of_degree_k,
    set_neighborhood,
)
from grinpy.invariants.dsi import sub_k_domination_number, sub_total_domination_number
from grinpy.invariants.independence import is_independent_set

__all__ = [
    "is_k_dominating_set",
    "is_total_dominating_set",
    "is_connected_k_dominating_set",
    "is_connected_dominating_set",
    "min_k_dominating_set",
    "min_dominating_set",
    "min_total_dominating_set",
    "min_connected_k_dominating_set",
    "min_connected_dominating_set",
    "domination_number",
    "k_domination_number",
    "total_domination_number",
    "connected_k_domination_number",
    "connected_domination_number",
    "is_independent_k_dominating_set",
    "is_independent_dominating_set",
    "min_independent_k_dominating_set",
    "min_independent_dominating_set",
    "independent_k_domination_number",
    "independent_domination_number",
]


def is_k_dominating_set(G, nodes, k):
    """Return whether or not nodes comprises a k-dominating set.

    A *k-dominating set* is a set of nodes with the property that every
    node in the graph is either in the set or adjacent at least 1 and at
    most k nodes in the set.

    This is a generalization of the well known concept of a dominating
    set (take k = 1).

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    k : int
        A positive integer.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a k-dominating set, and
        False otherwise.

    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    if k < 1:
        raise ValueError("Expected k to be a positive integer.")
    # check if nbunch is an iterable; if not, convert to a list
    S = set(n for n in nodes if n in G)
    if k == 1:
        return is_dominating_set(G, S)
    else:
        # loop through the nodes in the complement of S and determine
        # if they are adjacent to atleast k nodes in S
        others = set(G.nodes()).difference(S)
        for v in others:
            if len(set(neighborhood(G, v)).intersection(S)) < k:
                return False
        # if the above loop completes, nbunch is a k-dominating set
        return True


def is_total_dominating_set(G, nodes):
    """Return whether or not nodes comprises a total dominating set.

    A * total dominating set* is a set of nodes with the property that
    every node in the graph is adjacent to some node in the set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise a k-dominating set, and
        False otherwise.

    """
    # exclude any nodes that aren't in G
    S = set(n for n in nodes if n in G)
    return set(set_neighborhood(G, S)) == set(G.nodes())


def is_connected_k_dominating_set(G, nodes, k):
    """Return whether or not *nodes* is a connected *k*-dominating set of *G*.

    A set *D* is a *connected k-dominating set* of *G* is *D* is a
    *k*-dominating set in *G* and the subgraph of *G* induced by *D* is
    a connected graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    k : int
        A positive integer

    Returns
    -------
    boolean
        True if *nbunch* is a connected *k*-dominating set in *G*, and false
        otherwise.

    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    if k < 1:
        raise ValueError("Expected k to be a positive integer.")
    S = set(n for n in nodes if n in G)
    H = G.subgraph(S)
    return is_connected(H) and is_k_dominating_set(G, S, k)


def is_connected_dominating_set(G, nodes):
    """Return whether or not *nodes* is a connected dominating set of *G*.

    A set *D* is a *connected dominating set* of *G* is *D* is a
    dominating set in *G* and the subgraph of *G* induced by *D* is a
    connected graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    Returns
    -------
    boolean
        True if *nbunch* is a connected *k*-dominating set in *G*, and false
        otherwise.

    """
    return is_connected_k_dominating_set(G, nodes, 1)


def min_k_dominating_set(G, k):
    """Return a smallest k-dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the
    sub-k-domination number of the graph, which was defined by Amos et
    al. and shown to be a tractable lower bound for the k-domination
    number.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    list
        A list of nodes in a smallest k-dominating set in the graph.

    References
    ----------
    D. Amos, J. Asplund, and R. Davila, The sub-k-domination number of a
    graph with applications to k-domination, *arXiv preprint
    arXiv:1611.02379*, (2016)

    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    if k < 1:
        raise ValueError("Expected k to be a positive integer.")
    # use the sub-k-domination number to compute a starting point for the
    # search range
    rangeMin = sub_k_domination_number(G, k)
    # loop through subsets of nodes of G in increasing order of size until a
    # dominating set is found
    for i in range(rangeMin, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_k_dominating_set(G, S, k):
                return list(S)


def min_connected_k_dominating_set(G, k):
    """Return a smallest connected k-dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    list
        A list of nodes in a smallest k-dominating set in the graph.

    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    if k < 1:
        raise ValueError("Expected k to be a positive integer.")
    # Only proceed with search if graph is connected
    if not is_connected(G):
        return []
    for i in range(1, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_connected_k_dominating_set(G, S, k):
                return list(S)


def min_connected_dominating_set(G, k):
    """Return a smallest connected dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest connected dominating set in the
        graph.

    """
    return min_connected_k_dominating_set(G, 1)


def min_dominating_set_bf(G):
    """Return a smallest dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the
    sub-domination number of the graph, which was defined by Amos et al.
    and shown to be a tractable lower bound for the k-domination number.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest dominating set in the graph.

    See Also
    --------
    min_k_dominating_set

    References
    ----------
    D. Amos, J. Asplund, B. Brimkov and R. Davila, The sub-k-domination
    number of a graph with applications to k-domination, *arXiv preprint
    arXiv:1611.02379*, (2016)

    """
    return min_k_dominating_set(G, 1)


def min_dominating_set_ilp(G):
    """Return a smallest dominating set in the graph.

    A dominating set in a graph *G* is a set *D* of nodes of *G* for
    which every node not in *D* has a neighbor in *D*.

    This method using integer programming to compute a smallest
    dominating set. It solves the following integer program: minimize

    .. math::

        \\sum_{v \\in V} x_v

    subject to

    ... math::

        x_v + \\sum_{u \\in N(v)} x_u \\geq 1 \\mathrm{ for all } v \\in V

    where *V* is the set of nodes of G and *N(v)* is the set of
    neighbors of the vertex *v*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    set
        A set of nodes in a smallest dominating set in the graph.

    See Also
    --------
    min_k_dominating_set

    """
    prob = LpProblem("min_total_dominating_set", LpMinimize)
    variables = {node: LpVariable("x{}".format(i + 1), 0, 1, LpBinary) for i, node in enumerate(G.nodes())}

    # Set the total domination number objective function
    prob += lpSum([variables[n] for n in variables])

    # Set constraints
    for node in G.nodes():
        combination = [variables[n] for n in variables if n in closed_neighborhood(G, node)]
        prob += lpSum(combination) >= 1

    prob.solve()
    solution_set = {node for node in variables if variables[node].value() == 1}
    return solution_set


def min_dominating_set(G, method="ilp"):
    """Return a smallest dominating set in the graph.

    A dominating set in a graph *G* is a set *D* of nodes of *G* for
    which every node not in *D* has a neighbor in *D*.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    method: string
        The method to use for finding a minimum dominating set. Use
        'ilp' for integer linear program or 'bf' for brute force.
        Defaults to 'ilp'.

    Returns
    -------
    set
        A set of nodes in a smallest dominating set in the graph.

    See Also
    --------
    min_k_dominating_set

    """
    dominating_set_func = {"bf": min_dominating_set_bf, "ilp": min_dominating_set_ilp}.get(method, None)

    if dominating_set_func:
        return dominating_set_func(G)

    raise ValueError('Invalid `method` arguemnt "{}"'.format(method))


def min_total_dominating_set_bf(G):
    """Return a smallest total dominating set in the graph.

    The method to compute the set is brute force except that the subsets
    searched begin with those whose cardinality is equal to the
    sub-total-domination number of the graph, which was defined by
    Davila and shown to be a tractable lower bound for the k-domination
    number.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest total dominating set in the graph.

    References
    ----------
    R. Davila, A note on sub-total domination in graphs. *arXiv preprint
    arXiv: 1701.07811*, (2017)

    """
    # use naive lower bound for domination to compute a starting point
    # for the search range
    rangeMin = sub_total_domination_number(G)

    if number_of_nodes_of_degree_k(G, 0) > 0:
        return set()

    for i in range(rangeMin, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_total_dominating_set(G, S):
                return list(S)


def min_total_dominating_set_ilp(G):
    """Return a smallest total dominating set in the graph.

    This method solves an integer linear program in order to find a
    smallest total dominating set. It solves the following integer
    program: minimize

    .. math::

        \\sum_{v \\in V} x_v

    subject to

    ... math::

        \\sum_{u \\in N(v)} x_u \\geq 1 \\mathrm{ for all } v \\in V

    where *V* is the set of nodes of G and *N(v)* is the set of
    neighbors of the vertex *v*.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    set
        A set of nodes in a smallest total dominating set in the graph.

    References
    ----------
    R. Davila, A note on sub-total domination in graphs. *arXiv preprint
    arXiv: 1701.07811*, (2017)

    """
    prob = LpProblem("min_total_dominating_set", LpMinimize)
    variables = {node: LpVariable("x{}".format(i + 1), 0, 1, LpBinary) for i, node in enumerate(G.nodes())}

    # Set the total domination number objective function
    prob += lpSum([variables[n] for n in variables])

    # Set constraints
    for node in G.nodes():
        combination = [variables[n] for n in variables if n in neighborhood(G, node)]
        prob += lpSum(combination) >= 1

    prob.solve()
    solution_set = {node for node in variables if variables[node].value() == 1}
    return solution_set


def min_total_dominating_set(G, method="ilp"):
    """Return a smallest total dominating set in the graph.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    method: string
        The method to use for finding a minimum total dominating set.
        Use 'ilp' for integer linear program or 'bf' for brute force.
        Defaults to 'ilp'.

    Returns
    -------
    set
        A set of nodes in a smallest total dominating set in the graph.

    References
    ----------
    R. Davila, A note on sub-total domination in graphs. *arXiv preprint
    arXiv: 1701.07811*, (2017)

    """
    total_dominating_set_func = {"bf": min_total_dominating_set_bf, "ilp": min_total_dominating_set_ilp}.get(
        method, None
    )

    if total_dominating_set_func:
        return total_dominating_set_func(G)

    raise ValueError('Invalid `method` argument "{}"'.format(method))


def domination_number(G, method="ilp"):
    """Return the domination number the graph.

    The * domination number * of a graph is the cardinality of a smallest
    dominating set of nodes in the graph.

    This method calls the `min_dominating_set_ip` method in order to
    compute a smallest dominating set, then returns the length of that
    set.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    method: string
        The method to use for calculating the domination number. Use
        'ilp' for integer linear program or 'bf' for brute force.
        Defaults to 'ilp'.

    Returns
    -------
    int
        The domination number of the graph.

    See Also
    --------
    min_dominating_set, k_domination_number

    """
    try:
        return len(min_dominating_set(G, method=method))
    except ValueError:
        raise


def k_domination_number(G, k):
    """Return the k-domination number the graph.

    The * k-domination number * of a graph is the cardinality of a
    smallest k-dominating set of nodes in the graph.

    The method to compute this number is modified brute force.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The k-domination number of the graph.

    See Also
    --------
    min_k_dominating_set, domination_number

    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    if k < 1:
        raise ValueError("Expected k to be a positive integer.")
    return len(min_k_dominating_set(G, k))


def connected_k_domination_number(G, k):
    """Return the connected k-domination number the graph.

    The * connected k-domination number * of a graph is the cardinality
    of a smallest k-dominating set of nodes in the graph that induces a
    connected subgraph.

    The method to compute this number is brute force.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The connected k-domination number of the graph.

    """
    # check that k is a positive integer
    if not float(k).is_integer():
        raise TypeError("Expected k to be an integer.")
    k = int(k)
    if k < 1:
        raise ValueError("Expected k to be a positive integer.")
    return len(min_connected_k_dominating_set(G, k))


def connected_domination_number(G):
    """Return the connected domination number the graph.

    The * connected domination number * of a graph is the cardinality of a
    smallest dominating set of nodes in the graph that induces a
    connected subgraph.

    The method to compute this number is brute force.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The connected domination number of the graph.

    """
    return connected_k_domination_number(G, 1)


def total_domination_number(G, method="ilp"):
    """Return the total domination number the graph.

    The * total domination number * of a graph is the cardinality of a
    smallest total dominating set of nodes in the graph.

    The method to compute this number is modified brute force.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    method: string
        The method to use for calulating the total domination number.
        Use 'ilp' for integer linear program or 'bf' for brute force.
        Defaults to 'ilp'.

    Returns
    -------
    int
        The total domination number of the graph.

    """
    try:
        return len(min_total_dominating_set(G, method=method))
    except ValueError as exc:
        raise ValueError(exc)


def is_independent_k_dominating_set(G, nodes, k):
    """Return whether or not *nodes * is an independent k-dominating set in *G.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    nodes: list, set
        An iterable container of nodes in G.

    k: int
        A positive integer.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise an independent k-dominating
        set, and False otherwise.

    """
    return is_k_dominating_set(G, nodes, k) and is_independent_set(G, nodes)


def is_independent_dominating_set(G, nodes):
    """Return whether or not *nodes * is an independent k-dominating set in *G*.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    nodes: list, set
        An iterable container of nodes in G.

    Returns
    -------
    boolean
        True if the nodes in nbunch comprise an independent dominating
        set, and False otherwise.

    """
    return is_k_dominating_set(G, nodes, 1) and is_independent_set(G, nodes)


def min_independent_k_dominating_set(G, k):
    """Return a smallest independent k-dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest independent k-dominating set in
        the graph.

    """
    # loop through subsets of nodes of G in increasing order of size until a
    # total dominating set is found
    for i in range(1, number_of_nodes(G) + 1):
        for S in combinations(nodes(G), i):
            if is_independent_k_dominating_set(G, S, k):
                return list(S)


def min_independent_dominating_set_bf(G):
    """Return a smallest independent dominating set in the graph.

    The method to compute the set is brute force.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes in a smallest independent dominating set in the
        graph.

    """
    return min_independent_k_dominating_set(G, 1)


def min_independent_dominating_set_ilp(G):
    """Return a smallest independent dominating set in the graph.

    This method solves an integer program to compute a smallest
    independent dominating set. It solves the following integer program:
    minimize

    .. math::

        \\sum_{v \\in V} x_v

    subject to

    ... math::

        x_v + \\sum_{u \\in N(v)} x_u \\geq 1 \\mathrm{ for all } v \\in V
        \\sum_{\\{u, v\\} \\in E} x_u + x_v \\leq 1 \\mathrm{ for all } e \\in E

    where *E* and *V* are the set of edges and nodes of G, and *N(v)* is
    the set of neighbors of the vertex *v*.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    set
        A set of nodes in a smallest independent dominating set in the
        graph.

    """
    prob = LpProblem("min_total_dominating_set", LpMinimize)
    variables = {node: LpVariable("x{}".format(i + 1), 0, 1, LpBinary) for i, node in enumerate(G.nodes())}

    # Set the domination number objective function
    prob += lpSum(variables)

    # Set constraints for domination
    for node in G.nodes():
        combination = [variables[n] for n in variables if n in closed_neighborhood(G, node)]
        prob += lpSum(combination) >= 1

    # Set constraints for independence
    for e in G.edges():
        prob += variables[e[0]] + variables[e[1]] <= 1

    prob.solve()
    solution_set = {node for node in variables if variables[node].value() == 1}
    return solution_set


def min_independent_dominating_set(G, method="ilp"):
    """Return a smallest independent dominating set in the graph.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    method: string
        The method to use for finding a smallest independent dominating
        set. Use 'ilp' for integer linear program or 'bf' for brute
        force. Defaults to 'ilp'.

    Returns
    -------
    set
        A set of nodes in a smallest independent dominating set in the
        graph.

    """
    independent_dominating_set_func = {
        "bf": min_independent_dominating_set_bf,
        "ilp": min_independent_dominating_set_ilp,
    }.get(method, None)

    if independent_dominating_set_func:
        return independent_dominating_set_func(G)

    raise ValueError('Invalid `method` argument "{}"'.format(method))


def independent_k_domination_number(G, k):
    """Return the independnet k-domination number the graph.

    The * independent k-domination number * of a graph is the cardinality
    of a smallest independent k-dominating set of nodes in the graph.

    The method to compute this number is brute force.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The independent k-domination number of the graph.

    """
    return len(min_independent_k_dominating_set(G, k))


def independent_domination_number(G, method="ilp"):
    """Return the independnet domination number the graph.

    The * independent domination number * of a graph is the cardinality of
    a smallest independent dominating set of nodes in the graph.

    Parameters
    ----------
    G: NetworkX graph
        An undirected graph.

    method: string
        The method to use for calculating the independent dominationg
        number. Use 'ilp' for integer linear program or 'bf' for brute
        force. Defaults to 'ilp'.

    Returns
    -------
    int
        The independent domination number of the graph.

    """
    try:
        return len(min_independent_dominating_set(G, method=method))
    except ValueError:
        raise
